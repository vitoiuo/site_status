
from django.core.management import BaseCommand
from core.site_checker import sites_checker

class Command(BaseCommand):

    help = 'Acessa todas as urls armazenadas no site e retorna a HttResponse'
    # def add_arguments(self, parser):
    #     parser.add_argument('url', type=str, )
    #     parser.add_argument('--delete', '-d', action="store_true")
    #     Nomeado
    #     parser.add_argument('--nome', '-n')
    def handle(self, *args, **options):
          sites_checker()
            
        # if options['delete']:
        # # messages
        #     self.stdout.write(self.style.SUCCESS('Teste'))
        #     self.stdout.write(self.style.ERROR('Teste'))
        #     self.stdout.write(self.style.WARNING('Teste'))
        #     self.stderr.write('Erro')
        # else:
        #     raise CommandError('PERIGO')
