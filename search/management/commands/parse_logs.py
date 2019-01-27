from django.core.management.base import BaseCommand, CommandError

from search.log_parser import LogParser

class Command(BaseCommand):
    help = 'Parses log files'

    def add_arguments(self, parser):
        parser.add_argument('log_file_name', nargs='+', type=str)

    def handle(self, *args, **options):

        for f in options['log_file_name']:
            log_parser = LogParser(f)
            assert False, log_parser.parse_log_file()

            self.stdout.write(self.style.SUCCESS('Parsed file: {}'.format(f)))
