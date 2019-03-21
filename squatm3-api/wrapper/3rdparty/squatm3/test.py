from modules.Whoiser import Whoiser
from modules.Classes import Domain
from modules.Output import outputer

complete_domain = "gogo56.com"
result_domain = Domain.Domain()
w = Whoiser.Whoiser()
w.get_info(complete_domain)
#print(w.__dict__)
#result_domain.creation_date = w.creation_date
#result_domain.expiration_date = w.expiration_date

#print(w.whois_info.__dict__)
print("#####")

outputer.print_json_to_console("JUST WHOIS", result_domain)
