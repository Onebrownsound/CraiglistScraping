
import cPickle as pickle
import time
from craigslist import CraigslistForSale,get_all_sites

#Configure prior to running
#CL urls usually work by https://YOUR_STATE.cragilist.org/YOUR_AREA
YOUR_STATE='longisland'
YOUR_AREA='lgi'





def scrape():


    with open('data.pickle','rb') as fp:
        cl_listings = pickle.load(fp)



    #scrape for data
    cl_query = CraigslistForSale(site=YOUR_STATE, filters={'max_price':250,'query':'ikea desk'})
    for result in cl_query.get_results(sort_by='newest'):
        print(result)
        if result not in cl_listings:
            cl_listings.append(result)

    with open('data.pickle','wb') as fp:
        pickle.dump(cl_listings,fp)










while True:
   scrape()
   print('loop completed sleeping for 10 minutes')
   time.sleep(600)


