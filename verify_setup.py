#!/usr/bin/env python
"""
Quick verification script to check if the Django project is set up correctly.
Run this after setting up the project to verify all components are in place.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_backend_caching_property_listings.settings')
django.setup()

from properties.models import Property
from properties.utils import get_all_properties, get_redis_cache_metrics
from django.core.cache import cache

def verify_setup():
    """Verify that all components are set up correctly."""
    print("=" * 60)
    print("Django Property Listings - Setup Verification")
    print("=" * 60)
    
    # Check model
    print("\n✓ Property model imported successfully")
    print(f"  Model fields: {[f.name for f in Property._meta.fields]}")
    
    # Check cache
    try:
        cache.set('test_key', 'test_value', 10)
        value = cache.get('test_key')
        if value == 'test_value':
            print("✓ Redis cache connection working")
        else:
            print("✗ Redis cache connection issue")
    except Exception as e:
        print(f"✗ Redis cache connection error: {e}")
    
    # Check utils functions
    try:
        properties = get_all_properties()
        print(f"✓ get_all_properties() function working (found {len(properties)} properties)")
    except Exception as e:
        print(f"✗ get_all_properties() error: {e}")
    
    try:
        metrics = get_redis_cache_metrics()
        print("✓ get_redis_cache_metrics() function working")
        print(f"  Cache hits: {metrics.get('keyspace_hits', 0)}")
        print(f"  Cache misses: {metrics.get('keyspace_misses', 0)}")
    except Exception as e:
        print(f"✗ get_redis_cache_metrics() error: {e}")
    
    # Check signals
    try:
        from properties.signals import invalidate_property_cache_on_save
        print("✓ Cache invalidation signals imported successfully")
    except Exception as e:
        print(f"✗ Signals import error: {e}")
    
    print("\n" + "=" * 60)
    print("Verification complete!")
    print("=" * 60)

if __name__ == '__main__':
    verify_setup()
