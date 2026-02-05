import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone
from django.conf import settings
import os


def generate_qr_code(short_url_instance, request=None):
    """
    Generate QR code for a ShortUrl instance
    
    Args:
        short_url_instance: ShortUrl model instance
        request: Django request object to build full URL
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Build the full short URL
        if request:
            full_url = request.build_absolute_uri(f'/{short_url_instance.short_code}/')
        else:
            # Fallback if no request object
            domain = getattr(settings, 'SITE_DOMAIN', 'localhost:8000')
            protocol = 'https' if getattr(settings, 'USE_HTTPS', False) else 'http'
            full_url = f"{protocol}://{domain}/{short_url_instance.short_code}/"
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or less errors can be corrected
            box_size=10,  # Controls how many pixels each "box" of the QR code is
            border=4,  # Controls how many boxes thick the border should be
        )
        
        # Add data to QR code
        qr.add_data(full_url)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Save image to BytesIO
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        buffer.seek(0)
        
        # Generate filename
        filename = f"qr_{short_url_instance.short_code}_{timezone.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        # Save to model
        short_url_instance.qr_code_image.save(
            filename,
            ContentFile(buffer.getvalue()),
            save=False
        )
        
        # Update generation timestamp
        short_url_instance.qr_code_generated_at = timezone.now()
        short_url_instance.save(update_fields=['qr_code_image', 'qr_code_generated_at'])
        
        return True
        
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return False


def get_full_short_url(short_url_instance, request=None):
    """
    Get the full URL for a short code
    
    Args:
        short_url_instance: ShortUrl model instance
        request: Django request object to build full URL
    
    Returns:
        str: Full URL for the short code
    """
    if request:
        return request.build_absolute_uri(f'/{short_url_instance.short_code}/')
    else:
        # Fallback if no request object
        domain = getattr(settings, 'SITE_DOMAIN', 'localhost:8000')
        protocol = 'https' if getattr(settings, 'USE_HTTPS', False) else 'http'
        return f"{protocol}://{domain}/{short_url_instance.short_code}/"


def delete_qr_code_file(short_url_instance):
    """
    Delete QR code file from storage
    
    Args:
        short_url_instance: ShortUrl model instance
    """
    try:
        if short_url_instance.qr_code_image:
            # Delete the file from storage
            if os.path.isfile(short_url_instance.qr_code_image.path):
                os.remove(short_url_instance.qr_code_image.path)
            
            # Clear the field
            short_url_instance.qr_code_image = None
            short_url_instance.qr_code_generated_at = None
            short_url_instance.save(update_fields=['qr_code_image', 'qr_code_generated_at'])
            
        return True
    except Exception as e:
        print(f"Error deleting QR code file: {e}")
        return False


def regenerate_qr_code(short_url_instance, request=None):
    """
    Regenerate QR code for a ShortUrl instance (delete old one and create new)
    
    Args:
        short_url_instance: ShortUrl model instance
        request: Django request object to build full URL
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Delete existing QR code
    delete_qr_code_file(short_url_instance)
    
    # Generate new QR code
    return generate_qr_code(short_url_instance, request)