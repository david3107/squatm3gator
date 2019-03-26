<<<<<<< HEAD
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
=======
import whois
from modules.Whoiser import Whoiser
from modules.Classes import Domain

#w = Whoiser.Whoiser("google.com")
#cr_date = str(w.get_creation_date())
#exp_date = str(w.get_expiration_date())
#domain = whois.query('google.com')
#print(domain.__dict__)
#print(cr_date + "   #.   " + exp_date) 

complete_domain = "google.com"
result_domain = Domain.Domain()                    
# whois info
w = Whoiser.Whoiser(complete_domain)
result_domain.creation_date = w.get_creation_date()
result_domain.expiry_date = w.get_expiration_date()
cr_date = str(result_domain.creation_date)
exp_date = str(result_domain.expiry_date)

print(cr_date + "   #.   " + exp_date)
>>>>>>> e4b3e66e5df9733e31e4a4ca4d05dac370e315f9
