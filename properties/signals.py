from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
import logging
from .models import Property

logger = logging.getLogger('properties')


@receiver(post_save, sender=Property)
def invalidate_property_cache_on_save(sender, instance, **kwargs):
    """
    Invalidate the all_properties cache when a property is created or updated.
    """
    cache.delete('all_properties')
    logger.info('Cache invalidated: Property saved (create/update)')


@receiver(post_delete, sender=Property)
def invalidate_property_cache_on_delete(sender, instance, **kwargs):
    """
    Invalidate the all_properties cache when a property is deleted.
    """
    cache.delete('all_properties')
    logger.info('Cache invalidated: Property deleted')
