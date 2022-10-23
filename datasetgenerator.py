# importing libraries as needed
import csv
import random
  
# create a csv file named "abc" that contains our dataset
with open('testdataset5.csv', 'w', newline ='') as f: 
    file = csv.writer(f)
    file.writerow(["landing_page_id","campaign_id","traffic_source_id","visitor_device_hardware_family","visitor_device_hardware_model","visitor_device_hardware_vendor","visitor_device_os_family","visitor_device_os_vendor","visitor_device_type","visitor_geo_location_cityName","visitor_geo_location_connection_type","visitor_geo_location_countryCode","visitor_geo_location_isp","visitor_geo_location_regionName","visitor_tokens_adh","visitor_tokens_cadid","visitor_tokens_adi"])
      
    # generate rows as much as wanted, we need to improve the inputs and the links bettwen columns
    for i in range (1, 2001) : 
        landing_page_id=['6275efd926bbbd2607aaa956','62566aa432b19a0164d802be','62e56f8c33d89f001ab29ff4']                       
        campaign_id =['62b5ad1b33eed8001ec4ca44','62b9ebe8a32cba001c02ffac']
        traffic_source_id =['5e46d6787810b90011c91204']
        visitor_device_hardware_family =['iPhone', 'Emulator', 'Macintosh','Galaxy Note9','Galaxy S8+','Galaxy S9','Galaxy S9+','Galaxy S7','Galaxy S8','Galaxy S20 FE 5G','one 5G UW','one 5G UW','edge+']
        visitor_device_hardware_model=['iPhone','Unknown','Macintosh','SM-N960U','one 5G UW','edge+','SM-G930V','Redmi Note 5 Pro','S42','S6003L','SC-03G','SM-A515F','iPad']
        visitor_device_hardware_vendor=['Apple','Unknown','Samsung','Motorola']
        visitor_device_os_family=['iOS','macOS','Windows','ChromeOS','Linux','Ubuntu','Android','iPadOS','Unknown']
        visitor_device_os_vendor=['Apple','Microsoft','Google','Unknown']
        visitor_device_browser=['Mobile Safari','Chrome','Safari','Yandex.Browser for Android','Edge (Chromium) for Windows,','GoogleMobile for iOS','Seznam For Android','Pale Moon','DuckDuckGo for iOS','DuckDuckGo for iOS (Mobile in desktop mode)','Kindle-Silk','Pinterest for iOS','Opera Mobile','Web Light','Unknown Android App','Unknown Crawler']
        visitor_device_os_version=['15.3.1','10.0','10.15.6','8.1','15.6','15.5','7','9','11']
        visitor_device_type=['Desktop','Phone']
        visitor_geo_location_cityName=['Charleston','Oakland','Silver Spring','Placerville','South Gate','Denver','Voorhees Township','Ontario','Irving','Hagerstown','Los Angeles','Laguna Hills','San Francisco','Sugar Land','Dallas','Melbourne','Oxon Hill','Phillipsburg','Tucson','Honolulu','Irvine','Katy','Palmdale','Vineyard Haven','Fall River','Gaithersburg','South Weymouth','San Diego','Bridgeport','Kerrville','Manteca','Corte Madera','Hyannis','Boca Raton','Hawkins','Thousand Oaks','Philadelphia','Sacramento','Scottsdale','Bend','Chandler','Champaign','Compton','Spring','Lynnfield','Newton Center','Plaistow','Newton','Sunnyvale','Sonoma','Park Ridge','San Pablo','Costa Mesa','Moorpark','Lady Lake','Sedro-Woolley','Corte Madera','La Jolla','Miami','Cypress','Hayward','Cockeysville','Glen Burnie','Grand Junction','Marblehead','Phoenix','Des Plaines']
        visitor_geo_location_connection_type=['Cable/DSL','Corporate','Cellular']
        visitor_geo_location_countryCode=['US']
        visitor_geo_location_isp=['Consolidated Communications','AT&T U-verse','Verizon Fios','AT&T Wireless','Lightower Fiber Networks I, LLC','Comcast Cable','Starlink','Spectrum','Antietam Broadband','Cox Communications','Cogent Communications','Windstream Communications','Switch','PenTeleData','Hawaiian Telcom','Partners HealthCare System','Optimum Online','Hill Country Telephone Cooperative, Inc.','Hotwire Communications','Etex Communications, LLC','Frontier Communications','Towerstream I','iCloud Private Relay','Isomedia','TDS Telecom','Verizon Wireless','CenturyLink','Hilltop Broadband','Tata Communications (america)','Amazon.com','WideOpenWest','Optimum WiFi']
        visitor_geo_location_regionName=['Illinois','California','Maryland','Colorado','New Jersey','Texas','New Jersey','Arizona','Hawaii','Massachusetts','Connecticut','Pennsylvania','Washington','Oregon','New Hampshire']
        visitor_tokens_adh=['regcovsolbattbackcity','regwillcoverowninzipcode','{AD_HEADLINE}']
        visitor_tokens_cadid=['4N30ZrVUO','x6TAVXa-H','gzNN2JgPTX','{AD_ID}'] 
        visitor_tokens_adi=['tsbatout','solarpergola','manroofsolar','{AD_IMAGE}']
        converted_yes=['0','1']
        converted_no=['0','1']
        file.writerow([random.choice(landing_page_id), random.randint(15, 65), 
                       random.sample(campaign_id, 2), random.choice(visitor_device_hardware_family),random.choice(visitor_device_hardware_model),random.choice(visitor_device_hardware_vendor),random.choice(visitor_device_os_family),random.choice(visitor_device_os_vendor),random.choice(visitor_device_type),random.choice(visitor_geo_location_cityName),random.choice(visitor_geo_location_connection_type),random.choice(visitor_geo_location_countryCode),random.choice(visitor_geo_location_isp),random.choice(visitor_geo_location_regionName),random.choice(visitor_tokens_adh),random.choice(visitor_tokens_cadid),random.choice(converted_yes),random.choice(converted_no)])
