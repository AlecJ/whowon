import csv
from src.api.service import create_battle
from src.util import loggingFactory, session_scope

_getLogger = loggingFactory('seed')


def seed_battles(csv_file_path):
    '''
    Imports a CSV file of battles into the database.

    :param csv_file_path: string, path to csv file
    :return: None
    '''
    logger = _getLogger('seed_battles')

    
    logger.debug('Opening {} as csv'.format(csv_file_path))
    with open(csv_file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # insert each row into the database
            try:
                with session_scope() as session:
                    result = create_battle(
                        session,
                        row.get('battleName'),
                        row.get('date'),
                        row.get('location'),
                        row.get('answer'),
                        row.get('belligerentA'),
                        row.get('belligerentB'),
                        row.get('leaderAName'),
                        row.get('leaderBName'),
                        row.get('leaderAImageLink'),
                        row.get('leaderBImageLink'),
                        row.get('wikipediaBlurb'),
                        row.get('wikipediaLink'),
                    )
                    if result:
                        logger.debug('Row added successfully.')
                    else:
                        logger.error('\nError adding row: \n{}'.format(row))
            except Exception as e:
                logger.error(e)