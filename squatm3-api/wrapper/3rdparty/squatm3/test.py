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
