# purge_rgpd.py
import logging
from datetime import datetime, timedelta

from database import get_user_data, delete_user_data
from analytics import anonymize_data
from audit import log_purge_event

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
DATA_RETENTION_PERIOD = timedelta(days=365)  # 1 year retention period

def purge_old_data():
    """
    Purge user data that is older than the retention period.
    """
    current_time = datetime.utcnow()
    cutoff_time = current_time - DATA_RETENTION_PERIOD

    # Fetch user data that is older than the retention period
    old_data = get_user_data(cutoff_time)

    for user_data in old_data:
        # Anonymize data for analytics before deletion
        anonymized_data = anonymize_data(user_data)
        
        # Delete user data from the database
        delete_user_data(user_data['user_id'])

        # Log the purge event for audit purposes
        log_purge_event(user_data['user_id'], current_time)

        logging.info(f"Purged data for user ID: {user_data['user_id']}")

if __name__ == "__main__":
    try:
        purge_old_data()
        logging.info("Data purge completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during data purge: {e}")
        raise