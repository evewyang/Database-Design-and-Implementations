# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

## Dataset Details
### 1) Origin
The data is adopted from the website [Inside Airbnb](http://insideairbnb.com/get-the-data.html). The data behind the Inside Airbnb site is sourced from publicly available information from the Airbnb site. The data has been analyzed, cleansed and aggregated where appropriate to faciliate public discussion. I select the city  Zurich, Zürich, Switzerland for analysis. To visual the data in a map, click [here](http://insideairbnb.com/zurich/). 
### 2) Format
The data is downloaded from the website as listings.csv.gz, a csv file compressed with gzip compressino, and decompressed and saved in the `data` directory in CSV format as [listings.csv](https://github.com/dbdesign-students-fall2021/airbnb-mongodb-analysis-evewyang/tree/main/data/listings.csv). 
### 3) Display
|id    |listing_url                        |scrape_id     |last_scraped|name                                            |description                                      |neighborhood_overview                                |picture_url                                                                                           |host_id|host_url                                 |host_name        |host_since|host_location                               |host_about                                              |host_response_time|host_response_rate|host_acceptance_rate|host_is_superhost|host_thumbnail_url                                                                                        |host_picture_url                                                                                             |host_neighbourhood|host_listings_count|host_total_listings_count|host_verifications|host_has_profile_pic|host_identity_verified|neighbourhood                        |neighbourhood_cleansed|neighbourhood_group_cleansed|latitude|longitude|property_type                   |room_type      |accommodates|bathrooms|bathrooms_text  |bedrooms|beds|amenities                   |price  |minimum_nights|maximum_nights|minimum_minimum_nights|maximum_minimum_nights|minimum_maximum_nights|maximum_maximum_nights|minimum_nights_avg_ntm|maximum_nights_avg_ntm|calendar_updated|has_availability|availability_30|availability_60|availability_90|availability_365|calendar_last_scraped|number_of_reviews|number_of_reviews_ltm|number_of_reviews_l30d|first_review|last_review|review_scores_rating|review_scores_accuracy|review_scores_cleanliness|review_scores_checkin|review_scores_communication|review_scores_location|review_scores_value|license|instant_bookable|calculated_host_listings_count|calculated_host_listings_count_entire_homes|calculated_host_listings_count_private_rooms|calculated_host_listings_count_shared_rooms|reviews_per_month|
|------|-----------------------------------|--------------|------------|------------------------------------------------|-------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------|-----------------------------------------|-----------------|----------|--------------------------------------------|--------------------------------------------------------|------------------|------------------|--------------------|-----------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------|-------------------|-------------------------|------------------|--------------------|----------------------|-------------------------------------|----------------------|----------------------------|--------|---------|--------------------------------|---------------|------------|---------|----------------|--------|----|----------------------------|-------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------|----------------|---------------|---------------|---------------|----------------|---------------------|-----------------|---------------------|----------------------|------------|-----------|--------------------|----------------------|-------------------------|---------------------|---------------------------|----------------------|-------------------|-------|----------------|------------------------------|-------------------------------------------|--------------------------------------------|-------------------------------------------|-----------------|
|73282 |https://www.airbnb.com/rooms/73282 |20211028222550|2021-10-28  |Clean, central, quiet                           |Arty neighborhood...                             |                                                     |https://a0.muscache.com/pictures/481072/abd94c69_original.jpg                                         |377532 |https://www.airbnb.com/users/show/377532 |Simona           |2011-02-04|Zurich, Zurich, Switzerland                 |I am from Italy and ...                                 |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/users/377532/profile_pic/1381299725/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/377532/profile_pic/1381299725/original.jpg?aki_policy=profile_x_medium      |                  |1                  |1                        |['email', ...     |t                   |t                     |                                     |Sihlfeld              |Kreis 3                     |47.37374|8.51957  |Entire rental unit              |Entire home/apt|4           |         |1 bath          |1       |1   |[“Essentials”...            |$100.00|3             |1825          |3                     |3                     |1825                  |1825                  |3.0                   |1825.0                |                |t               |0              |0              |0              |0               |2021-10-28           |49               |0                    |0                     |2012-09-24  |2019-03-28 |4.78                |4.87                  |4.8                      |4.84                 |4.93                       |4.71                  |4.61               |       |f               |1                             |1                                          |0                                           |0                                          |0.44             |
|86645 |https://www.airbnb.com/rooms/86645 |20211028222550|2021-10-28  |Stadium Letzigrund - by Airhome                 |Discover a boutique apartment ...                |Located 300 meters ...                               |https://a0.muscache.com/pictures/miso/Hosting-86645/original/d53da3fe-33c5-4b76-91ad-1a6797e4328e.jpeg|475053 |https://www.airbnb.com/users/show/475053 |James            |2011-03-31|Wherever you need me. Always happy to help. |Backed by an international team ...                     |within an hour    |99%               |93%                 |t                |https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_x_medium      |                  |36                 |36                       |['email', ...     |t                   |t                     |Zurich, Switzerland                  |Sihlfeld              |Kreis 3                     |47.38038|8.50461  |Entire rental unit              |Entire home/apt|3           |         |1 bath          |1       |2   |["Air conditioning", ...    |$180.00|1             |9999          |1                     |1                     |9999                  |9999                  |1.0                   |9999.0                |                |t               |0              |0              |0              |0               |2021-10-28           |50               |1                    |0                     |2013-11-17  |2021-07-16 |4.52                |4.67                  |4.7                      |4.64                 |4.77                       |4.6                   |4.47               |       |t               |18                            |18                                         |0                                           |0                                          |0.52             |
|143821|https://www.airbnb.com/rooms/143821|20211028222550|2021-10-28  |marvelous LOFT in SIHLCITY Zürich               |<b>The space</b><br />- 2.5 rooms on 2 floors ...|                                                     |https://a0.muscache.com/pictures/1012249/a4f3404d_original.jpg                                        |697307 |https://www.airbnb.com/users/show/697307 |Erhan            |2011-06-13|Zürich, Zurich, Switzerland                 |Hello everyone! ...                                     |within a few hours|100%              |0%                  |f                |https://a0.muscache.com/im/users/697307/profile_pic/1307991889/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/697307/profile_pic/1307991889/original.jpg?aki_policy=profile_x_medium      |                  |1                  |1                        |['email', ...     |t                   |t                     |                                     |Alt-Wiedikon          |Kreis 3                     |47.35724|8.52304  |Entire loft                     |Entire home/apt|2           |         |1.5 baths       |1       |2   |[“Hangers”,...              |$200.00|3             |365           |3                     |3                     |365                   |365                   |3.0                   |365.0                 |                |t               |26             |56             |86             |361             |2021-10-28           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |1                             |1                                          |0                                           |0                                          |                 |
|178448|https://www.airbnb.com/rooms/178448|20211028222550|2021-10-29  |a lovely place, top location                    |Very central location, ...                       |We live in one of the top locations ...              |https://a0.muscache.com/pictures/7d41e016-e818-4fe1-9d42-a5d0ae34bdda.jpg                             |854016 |https://www.airbnb.com/users/show/854016 |Delphine         |2011-07-22|Zurich, Zurich, Switzerland                 |I am a quiet, friendly and caring person...             |within a day      |100%              |0%                  |f                |https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_small      |https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_x_medium      |                  |1                  |1                        |['email', ...     |t                   |f                     |Zurich, Switzerland                  |Enge                  |Kreis 2                     |47.36565|8.52753  |Private room in rental unit     |Private room   |1           |         |1 bath          |1       |1   |["Wifi", ...                |$60.00 |5             |31            |5                     |5                     |31                    |31                    |5.0                   |31.0                  |                |t               |0              |0              |0              |0               |2021-10-29           |9                |0                    |0                     |2016-03-17  |2016-05-10 |4.89                |4.89                  |4.89                     |4.89                 |4.89                       |5.0                   |4.89               |       |f               |1                             |0                                          |1                                           |0                                          |0.13             |
|204586|https://www.airbnb.com/rooms/204586|20211028222550|2021-10-29  |very nice luxury city apartment                 |<b>The space</b><br />...                        |                                                     |https://a0.muscache.com/pictures/55486203/98347fab_original.jpg                                       |1004816|https://www.airbnb.com/users/show/1004816|Aicha            |2011-08-22|Zurich, Zurich, Switzerland                 |I'm a very active person, ...                           |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/users/1004816/profile_pic/1314029145/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1004816/profile_pic/1314029145/original.jpg?aki_policy=profile_x_medium     |                  |1                  |1                        |['email', ...     |t                   |f                     |                                     |Höngg                 |Kreis 10                    |47.40656|8.48465  |Private room in rental unit     |Private room   |1           |         |1 bath          |1       |1   |[“Wifi”,...                 |$200.00|3             |6             |3                     |3                     |6                     |6                     |3.0                   |6.0                   |                |t               |29             |59             |89             |364             |2021-10-29           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |1                             |0                                          |1                                           |0                                          |                 |
|216395|https://www.airbnb.com/rooms/216395|20211028222550|2021-10-28  |city studio, modern meets colonial              |<b>The space</b><br />...                        |                                                     |https://a0.muscache.com/pictures/2300000/49b5f1d7_original.jpg                                        |1116961|https://www.airbnb.com/users/show/1116961|Fabio            |2011-09-06|CH                                          |.                                                       |a few days or more|0%                |0%                  |f                |https://a0.muscache.com/im/users/1116961/profile_pic/1318457382/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1116961/profile_pic/1318457382/original.jpg?aki_policy=profile_x_medium     |                  |1                  |1                        |['email', 'phone']|t                   |f                     |                                     |Sihlfeld              |Kreis 3                     |47.3788 |8.50766  |Entire rental unit              |Entire home/apt|2           |         |1.5 baths       |1       |1   |["Wifi", ...                |$203.00|1             |365           |1                     |1                     |365                   |365                   |1.0                   |365.0                 |                |t               |30             |60             |90             |365             |2021-10-28           |0                |0                    |0                     |            |           |                    |                      |                         |                     |                           |                      |                   |       |f               |1                             |1                                          |0                                           |0                                          |                 |
|222565|https://www.airbnb.com/rooms/222565|20211028222550|2021-10-29  |Bedroom overlooking the lake near               |<b>The space</b><br />...                        |                                                     |https://a0.muscache.com/pictures/2299734/2509e4e8_original.jpg                                        |1155866|https://www.airbnb.com/users/show/1155866|Ysabel           |2011-09-14|Zurich, Zurich, Switzerland                 |We are a multicultural family. ...                      |within a day      |50%               |80%                 |f                |https://a0.muscache.com/im/users/1155866/profile_pic/1318532499/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/1155866/profile_pic/1318532499/original.jpg?aki_policy=profile_x_medium     |                  |2                  |2                        |[‘email’,...      |t                   |t                     |                                     |Wollishofen           |Kreis 2                     |47.33463|8.54117  |Private room in residential home|Private room   |2           |         |1 shared bath   |1       |1   |["Lock on bedroom door”,... |$69.00 |2             |90            |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |t               |0              |7              |7              |215             |2021-10-29           |222              |1                    |0                     |2012-04-03  |2019-06-01 |4.58                |4.65                  |4.32                     |4.82                 |4.83                       |4.76                  |4.6                |       |f               |1                             |0                                          |1                                           |0                                          |1.90             |
|227039|https://www.airbnb.com/rooms/227039|20211028222550|2021-10-28  |*Luxury Penthouse in the heart of trendy Zurich*|Modern and unique penthouse apartment ...        |Zurich is hip-circuit with the Swiss peacefulness!...|https://a0.muscache.com/pictures/28325669/6d4b0af4_original.jpg                                       |1184427|https://www.airbnb.com/users/show/1184427|Lucas            |2011-09-20|Zürich, Zurich, Switzerland                 |I'm a Swiss management consultant ...                   |within a day      |100%              |20%                 |f                |https://a0.muscache.com/im/pictures/user/23d284a1-b4ac-4e64-b894-9d4d2a50af66.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/23d284a1-b4ac-4e64-b894-9d4d2a50af66.jpg?aki_policy=profile_x_medium|                  |2                  |2                        |['email', ...     |t                   |t                     |Zurich, Canton of Zurich, Switzerland|Escher Wyss           |Kreis 5                     |47.38942|8.51881  |Entire condominium (condo)      |Entire home/apt|3           |         |1.5 baths       |2       |2   |["Outdoor furniture", ...   |$400.00|4             |14            |4                     |4                     |14                    |14                    |4.0                   |14.0                  |                |t               |23             |53             |83             |358             |2021-10-28           |28               |1                    |0                     |2014-08-18  |2019-12-20 |4.96                |5.0                   |4.93                     |4.96                 |4.93                       |4.93                  |4.86               |       |f               |1                             |1                                          |0                                           |0                                          |0.32             |
|283737|https://www.airbnb.com/rooms/283737|20211028222550|2021-10-29  |Best Location in Zurich Oldtown                 |The confortable, clean and authentic flat ...    |In my opinion the niederdorf is the most...          |https://a0.muscache.com/pictures/b0b6eedd-d96c-4b7c-9b8d-96a1ef7b6008.jpg                             |1477771|https://www.airbnb.com/users/show/1477771|Nuria            |2011-12-06|Zurich, Zurich, Switzerland                 |I’m a young widow ...                                   |within an hour    |93%               |83%                 |f                |https://a0.muscache.com/im/pictures/user/a986112c-5043-4566-8c64-a333d03878d1.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/a986112c-5043-4566-8c64-a333d03878d1.jpg?aki_policy=profile_x_medium|                  |2                  |2                        |[‘email',...      |t                   |t                     |Zurich, Switzerland                  |Rathaus               |Kreis 1                     |47.37284|8.54324  |Entire rental unit              |Entire home/apt|4           |         |1 bath          |2       |2   |["TV", ...                  |$159.00|4             |120           |4                     |4                     |1125                  |1125                  |4.0                   |1125.0                |                |t               |1              |14             |29             |193             |2021-10-29           |265              |24                   |4                     |2012-03-27  |2021-09-23 |4.47                |4.46                  |4.55                     |4.67                 |4.73                       |4.94                  |4.44               |       |f               |2                             |2                                          |0                                           |0                                          |2.27             |
|292351|https://www.airbnb.com/rooms/292351|20211028222550|2021-10-29  |120 sqM - 3 bedrooms + lounge in central Zurich |The condominium is 10 minutes ...                |Zurich Albisriederplatz is 1 minute walk...          |https://a0.muscache.com/pictures/36932097-1779-4dfd-b18e-94873c817c45.jpg                             |1513739|https://www.airbnb.com/users/show/1513739|Anil             |2011-12-17|Zurich, Zurich, Switzerland                 |I was born in India,...                                 |within an hour    |100%              |100%                |f                |https://a0.muscache.com/im/pictures/user/87c24f0f-d8d5-4469-a291-f8dcc80ea5e8.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/87c24f0f-d8d5-4469-a291-f8dcc80ea5e8.jpg?aki_policy=profile_x_medium|                  |1                  |1                        |[‘phone’,...      |t                   |t                     |Zürich, Switzerland                  |Sihlfeld              |Kreis 3                     |47.37896|8.50787  |Entire condominium (condo)      |Entire home/apt|10          |         |2.5 baths       |3       |9   |["Bathtub", ...             |$210.00|5             |1125          |5                     |5                     |1125                  |1125                  |5.0                   |1125.0                |                |t               |17             |38             |66             |66              |2021-10-29           |10               |1                    |1                     |2019-07-05  |2018-08-08 |4.56                |4.67                  |4.56                     |4.67                 |5.0                        |4.89                  |4.22               |       |t               |1                             |1                                          |0                                           |0                                          |0.35             |
|310964|https://www.airbnb.com/rooms/310964|20211028222550|2021-10-28  |Large Apartment - Center of Zurich              |<b>The space</b><br />...                        |Many theaters and museums ...                        |https://a0.muscache.com/pictures/3304245/14d3fae6_original.jpg                                        |1266114|https://www.airbnb.com/users/show/1266114|Kim              |2011-10-09|Zurich, Zurich, Switzerland                 |I live with my lovely 10 year old daughter and wife, ...|N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/pictures/user/c5f79a87-9e38-4344-ac69-000ba90aa1b7.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/c5f79a87-9e38-4344-ac69-000ba90aa1b7.jpg?aki_policy=profile_x_medium|                  |1                  |1                        |[‘email’,...      |t                   |t                     |Zurich, Switzerland                  |Hochschulen           |Kreis 1                     |47.36802|8.54813  |Entire rental unit              |Entire home/apt|6           |         |2 baths         |3       |2   |["Essentials", ...          |$360.00|7             |14            |7                     |7                     |14                    |14                    |7.0                   |14.0                  |                |t               |0              |0              |25             |300             |2021-10-28           |13               |0                    |0                     |2014-08-18  |2015-07-20 |4.92                |4.92                  |4.77                     |5.0                  |4.92                       |4.85                  |4.85               |       |f               |1                             |1                                          |0                                           |0                                          |0.15             |
|420869|https://www.airbnb.com/rooms/420869|20211028222550|2021-10-28  |Zürich - we like it!                            |<b>The space</b><br />...                        |                                                     |https://a0.muscache.com/pictures/4941282/e0aee01b_original.jpg                                        |2093123|https://www.airbnb.com/users/show/2093123|Mike             |2012-04-08|Zurich, Canton of Zurich, Switzerland       |Trainer für Cardiofitness, ...                          |within an hour    |100%              |0%                  |t                |https://a0.muscache.com/im/users/2093123/profile_pic/1335420456/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/2093123/profile_pic/1335420456/original.jpg?aki_policy=profile_x_medium     |                  |1                  |1                        |[‘email’,...      |t                   |t                     |                                     |Altstetten            |Kreis 9                     |47.39185|8.48432  |Private room in rental unit     |Private room   |1           |         |1 shared bath   |1       |1   |["Essentials", ...          |$58.00 |2             |14            |2                     |2                     |14                    |14                    |2.0                   |14.0                  |                |t               |0              |0              |0              |0               |2021-10-28           |95               |0                    |0                     |2013-02-16  |2019-10-09 |4.97                |4.9                   |4.95                     |4.95                 |4.98                       |4.88                  |4.89               |       |f               |1                             |0                                          |1                                           |0                                          |0.90             |
|438084|https://www.airbnb.com/rooms/438084|20211028222550|2021-10-29  |superurbanes schönes helles und ruhiges Zimmer  |das zimmer befindet sich im 1. ...               |es gibt rundherum ein grosses ...                    |https://a0.muscache.com/pictures/bcb674af-4e13-417a-bc9f-89ba0fa393d2.jpg                             |1241750|https://www.airbnb.com/users/show/1241750|Lia              |2011-10-03|Zürich, Zurich, Switzerland                 |i'm from zürich ...                                     |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/pictures/user/8c8b4890-f1ff-4198-8db5-1acdb84bc894.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/8c8b4890-f1ff-4198-8db5-1acdb84bc894.jpg?aki_policy=profile_x_medium|                  |0                  |0                        |[‘email’,...      |t                   |f                     |Zürich, Switzerland                  |Escher Wyss           |Kreis 5                     |47.38938|8.51844  |Private room in rental unit     |Private room   |2           |         |1.5 shared baths|1       |1   |["Essentials", ...          |$80.00 |1             |7             |1                     |1                     |7                     |7                     |1.0                   |7.0                   |                |t               |0              |27             |57             |332             |2021-10-29           |10               |2                    |0                     |2020-05-08  |2021-08-15 |4.8                 |4.5                   |4.9                      |4.8                  |5.0                        |4.9                   |4.8                |       |f               |1                             |0                                          |1                                           |0                                          |0.56             |
|551321|https://www.airbnb.com/rooms/551321|20211028222550|2021-10-28  |Zürich Charming Business/Holiday                |<b>The space</b><br />...                        |Health food bakers and coffee shop ...               |https://a0.muscache.com/pictures/7074633/a19a1875_original.jpg                                        |2709967|https://www.airbnb.com/users/show/2709967|Stephanie        |2012-06-22|Switzerland                                 |Hi! I speak English, ...                                |N/A               |N/A               |N/A                 |f                |https://a0.muscache.com/im/users/2709967/profile_pic/1340388557/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/2709967/profile_pic/1340388557/original.jpg?aki_policy=profile_x_medium     |                  |3                  |3                        |[‘email’,...      |t                   |t                     |Zurich, Canton of Zurich, Switzerland|Alt-Wiedikon          |Kreis 3                     |47.37008|8.51368  |Entire residential home         |Entire home/apt|2           |         |2.5 baths       |1       |1   |["Essentials", ...          |$115.00|2             |1125          |2                     |2                     |1125                  |1125                  |2.0                   |1125.0                |                |t               |0              |0              |29             |304             |2021-10-28           |22               |0                    |0                     |2013-04-13  |2013-04-07 |4.89                |4.74                  |4.89                     |4.95                 |4.95                       |4.84                  |4.68               |       |f               |1                             |1                                          |0                                           |0                                          |0.21             |
|577683|https://www.airbnb.com/rooms/577683|20211028222550|2021-10-29  |Modern & Spacious Garden-Suite in Zurich        |Modern and elegent Garden appartment ...         |very central but ...                                 |https://a0.muscache.com/pictures/090331a6-5088-4324-bd7a-212848881d6f.jpg                             |1240329|https://www.airbnb.com/users/show/1240329|Claudio          |2011-10-03|Zurich, Zurich, Switzerland                 |Italian Swiss living in Zurich...                       |within an hour    |100%              |33%                 |f                |https://a0.muscache.com/im/pictures/user/d656c0ff-8d61-4f95-8cd1-e7987d40b338.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/d656c0ff-8d61-4f95-8cd1-e7987d40b338.jpg?aki_policy=profile_x_medium|                  |2                  |2                        |[‘email’,...      |t                   |t                     |Zurich, Canton of Zurich, Switzerland|Höngg                 |Kreis 10                    |47.40419|8.49593  |Entire rental unit              |Entire home/apt|3           |         |1.5 baths       |1       |2   |["Outdoor furniture", ...   |$210.00|5             |30            |3                     |5                     |30                    |30                    |4.4                   |30.0                  |                |t               |8              |38             |62             |152             |2021-10-29           |7                |1                    |0                     |2012-11-25  |2018-04-16 |5.0                 |5.0                   |5.0                      |5.0                  |4.86                       |5.0                   |4.86               |       |f               |1                             |1                                          |0                                           |0                                          |0.06             |
|582946|https://www.airbnb.com/rooms/582946|20211028222550|2021-10-28  |Large Corner Room @ The Swiss Villa             |Are you a professional expat ...                 |There are 3 grocery stores,...                       |https://a0.muscache.com/pictures/8a5dac96-a990-48e5-80a5-46f1fa513999.jpg                             |44391  |https://www.airbnb.com/users/show/44391  |Caroline & Roland|2009-10-08|Zurich, Zurich, Switzerland                 |We are a Swiss couple ...                               |N/A               |N/A               |100%                |f                |https://a0.muscache.com/im/users/44391/profile_pic/1396889426/original.jpg?aki_policy=profile_small       |https://a0.muscache.com/im/users/44391/profile_pic/1396889426/original.jpg?aki_policy=profile_x_medium       |                  |3                  |3                        |[‘email’,...      |t                   |t                     |Zurich, ZH, Switzerland              |Fluntern              |Kreis 7                     |47.37795|8.55781  |Private room in villa           |Private room   |1           |         |1 private bath  |1       |1   |["Lock on bedroom door", ...|$120.00|10            |31            |10                    |10                    |31                    |31                    |10.0                  |31.0                  |                |t               |0              |0              |0              |0               |2021-10-28           |18               |0                    |0                     |2012-10-06  |2019-02-23 |5.0                 |5.0                   |5.0                      |4.94                 |4.94                       |4.94                  |5.0                |       |f               |3                             |0                                          |3                                           |0                                          |0.16             |
|606954|https://www.airbnb.com/rooms/606954|20211028222550|2021-10-28  |Big and quiet bedroom in green area!            |The flat is quiet and has 3 rooms....            |We live in a very green, ...                         |https://a0.muscache.com/pictures/46051013/dca45e60_original.jpg                                       |2659673|https://www.airbnb.com/users/show/2659673|Esther           |2012-06-17|Zürich, Zurich, Switzerland                 |I love traveling,...                                    |within a day      |100%              |0%                  |f                |https://a0.muscache.com/im/users/2659673/profile_pic/1406019455/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/2659673/profile_pic/1406019455/original.jpg?aki_policy=profile_x_medium     |                  |1                  |1                        |[‘email’,...      |t                   |t                     |Zurich, Switzerland                  |Sihlfeld              |Kreis 3                     |47.36867|8.49841  |Private room in rental unit     |Private room   |1           |         |1 shared bath   |1       |1   |["Hangers", ...             |$50.00 |2             |14            |2                     |2                     |14                    |14                    |2.0                   |14.0                  |                |f               |0              |0              |0              |0               |2021-10-28           |4                |0                    |0                     |2014-10-09  |2020-03-10 |5.0                 |5.0                   |4.5                      |5.0                  |4.75                       |4.75                  |4.75               |       |f               |1                             |0                                          |1                                           |0                                          |0.05             |
|610348|https://www.airbnb.com/rooms/610348|20211028222550|2021-10-28  |Duplex  Flat, 120 m2 7-8  persons               |<b>The space</b><br />...                        |Quiet, safe area, ...                                |https://a0.muscache.com/pictures/fad04441-d7be-4875-a8cf-510c4eb7a597.jpg                             |3026473|https://www.airbnb.com/users/show/3026473|Monica / Leandra |2012-07-23|Rekingen, Aargau, Switzerland               |We are a mother daughters team ...                      |within a few hours|100%              |100%                |t                |https://a0.muscache.com/im/pictures/user/d410dd8a-1a5f-45b2-95b0-e7aa3e9ab1f1.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/d410dd8a-1a5f-45b2-95b0-e7aa3e9ab1f1.jpg?aki_policy=profile_x_medium|                  |2                  |2                        |[‘email’,...      |t                   |t                     |Zurich, Canton of Zurich, Switzerland|Oerlikon              |Kreis 11                    |47.40703|8.55232  |Entire rental unit              |Entire home/apt|7           |         |2 baths         |4       |6   |["Hangers", ...             |$213.00|3             |1125          |3                     |3                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |13             |34             |56             |309             |2021-10-28           |96               |7                    |2                     |2015-09-11  |2021-09-28 |4.67                |4.8                   |4.86                     |4.93                 |4.91                       |4.72                  |4.54               |       |f               |1                             |1                                          |0                                           |0                                          |1.29             |
|620130|https://www.airbnb.com/rooms/620130|20211028222550|2021-10-29  |NB1: Charming 2-room apartment                  |<b>The space</b><br />...                        |                                                     |https://a0.muscache.com/pictures/f912367d-cb8b-4928-883c-1b64cdda6f7b.jpg                             |3072679|https://www.airbnb.com/users/show/3072679|Andrea           |2012-07-27|Zurich, Canton of Zurich, Switzerland       |Es freut mich, ...                                      |a few days or more|0%                |0%                  |f                |https://a0.muscache.com/im/users/3072679/profile_pic/1384192385/original.jpg?aki_policy=profile_small     |https://a0.muscache.com/im/users/3072679/profile_pic/1384192385/original.jpg?aki_policy=profile_x_medium     |                  |5                  |5                        |[‘email’,...      |t                   |t                     |                                     |Wipkingen             |Kreis 10                    |47.39232|8.52876  |Entire rental unit              |Entire home/apt|4           |         |1 bath          |1       |2   |[“Essentials”,...           |$185.00|3             |1125          |3                     |3                     |1125                  |1125                  |3.0                   |1125.0                |                |t               |0              |0              |0              |205             |2021-10-29           |25               |0                    |0                     |2019-04-22  |2019-04-13 |4.84                |4.92                  |4.88                     |5.0                  |4.92                       |4.96                  |4.72               |       |f               |5                             |5                                          |0                                           |0                                          |0.81             |
|644888|https://www.airbnb.com/rooms/644888|20211028222550|2021-10-29  |bright and great duplex in the heart of Zurich  |The apartment is bright, ...                     |Very nice people around                              |https://a0.muscache.com/pictures/9554554/d05c2bc6_original.jpg                                        |3228273|https://www.airbnb.com/users/show/3228273|Violetta         |2012-08-11|Zürich, Zurich, Switzerland                 |ENGLISH: I'm originally from Italy....                  |within a day      |50%               |13%                 |f                |https://a0.muscache.com/im/pictures/user/997fbe65-087b-46dc-9070-86fe43a0d3bd.jpg?aki_policy=profile_small|https://a0.muscache.com/im/pictures/user/997fbe65-087b-46dc-9070-86fe43a0d3bd.jpg?aki_policy=profile_x_medium|                  |0                  |0                        |[‘email’,...      |t                   |t                     |Zurich, Canton of Zurich, Switzerland|Hard                  |Kreis 4                     |47.38003|8.50829  |Private room in rental unit     |Private room   |3           |         |2 shared baths  |3       |7   |["Outdoor furniture", ...   |$65.00 |3             |300           |3                     |3                     |300                   |300                   |3.0                   |300.0                 |                |t               |1              |1              |1              |171             |2021-10-29           |16               |1                    |0                     |2013-04-01  |2021-08-08 |4.86                |4.86                  |4.86                     |4.93                 |4.79                       |4.64                  |4.71               |       |f               |1                             |0                                          |1                                           |0                                          |0.15             |


### 4) Problem and Data Scrubbing
Among 1825 data as rows, there are many records that have some fields of information filled by "N/A" or just left as blank. Some of them have rating scores missing, some of them have neighborhood information missing...these are important criteria when one try to book an Airbnb, so listings without explicit illustration of these should be dropped. Also, some columns/fileds are generally missing for all records, so leaving them in the chart becomes unnecessary. For example, 'calendar_updated' field is missing for all records and essencially provides arbitrary information even if it is not left blank; 'bathroom' field is redundant and mostly blank since 'bathrooms_text' field provide same and more explicit information, therefore removing such field is a natural act. Below shows the code piece in `main` executive function(view full codes in [munge.py](https://github.com/dbdesign-students-fall2021/airbnb-mongodb-analysis-evewyang/tree/main/munge.py)):
```python
def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/listings.csv')
    print(len(data))
    data = remove_mostly_empty_columns(data,'host_neighbourhood')
    data = remove_mostly_empty_columns(data,'license')
    data = remove_mostly_empty_columns(data,'calendar_updated')
    data = remove_mostly_empty_columns(data,'bathrooms')
    # munge it
    data = remove_rows_with_blank_fields(data)
    print(len(data))
    # save to the new csv file
    save_csv_data(data, 'data/listings_clean.csv')
```
## Analysis
### 1) show exactly two documents from the listings collection in any order
Use `find()` to get the document, and use `limit()` to set the number of document to be output, and sort the fetched documents by its 'id', in the ascending order using `sort({'id':1})`:
```
db.listings.find().limit(2).sort({'id': 1})
```
Output:
```
{ "_id" : ObjectId("6194703d051c47f3e6883fda"), "id" : 86645, "listing_url" : "https://www.airbnb.com/rooms/86645", "scrape_id" : NumberLong("20211028222550"), "last_scraped" : "2021-10-28", "name" : "Stadium Letzigrund - by Airhome", "description" : "Discover a boutique apartment...", "neighborhood_overview" : "Located 300 meters...", "picture_url" : "https://a0.muscache.com/pictures/miso/Hosting-86645/original/d53da3fe-33c5-4b76-91ad-1a6797e4328e.jpeg", "host_id" : 475053, "host_url" : "https://www.airbnb.com/users/show/475053", "host_name" : "James", "host_since" : "2011-03-31", "host_location" : "Wherever you need me. Always happy to help.", "host_about" : "Backed by an international team of guest support specialists and AI technology, James will be available for you 7/24 and always happy to help and assist you with your requests.", "host_response_time" : "within an hour", "host_response_rate" : "99%", "host_acceptance_rate" : "93%", "host_is_superhost" : "t", "host_thumbnail_url" : "https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_x_medium", "host_listings_count" : 36, "host_total_listings_count" : 36, "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id', 'work_email']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "Zurich, Switzerland", "neighbourhood_cleansed" : "Sihlfeld", "neighbourhood_group_cleansed" : "Kreis 3", "latitude" : 47.38038, "longitude" : 8.50461, "property_type" : "Entire rental unit", "room_type" : "Entire home/apt", "accommodates" : 3, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 2, "amenities" : "[\"Air conditioning\", \"Essentials\", \"Elevator\", \"Heating\", \"TV with standard cable\", \"Fire extinguisher\", \"Smart lock\", \"Smoke alarm\", \"Long term stays allowed\", \"Cable TV\", \"Hair dryer\", \"Shampoo\", \"Indoor fireplace\", \"Kitchen\", \"Wifi \\u2013 50 Mbps\"]", "price" : "$180.00", "minimum_nights" : 1, "maximum_nights" : 9999, "minimum_minimum_nights" : 1, "maximum_minimum_nights" : 1, "minimum_maximum_nights" : 9999, "maximum_maximum_nights" : 9999, "minimum_nights_avg_ntm" : 1, "maximum_nights_avg_ntm" : 9999, "has_availability" : "t", "availability_30" : 0, "availability_60" : 0, "availability_90" : 0, "availability_365" : 0, "calendar_last_scraped" : "2021-10-28", "number_of_reviews" : 50, "number_of_reviews_ltm" : 1, "number_of_reviews_l30d" : 0, "first_review" : "2013-11-17", "last_review" : "2021-07-16", "review_scores_rating" : 4.52, "review_scores_accuracy" : 4.67, "review_scores_cleanliness" : 4.7, "review_scores_checkin" : 4.64, "review_scores_communication" : 4.77, "review_scores_location" : 4.6, "review_scores_value" : 4.47, "instant_bookable" : "t", "calculated_host_listings_count" : 18, "calculated_host_listings_count_entire_homes" : 18, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.52 }
{ "_id" : ObjectId("6194703d051c47f3e6883fdb"), "id" : 178448, "listing_url" : "https://www.airbnb.com/rooms/178448", "scrape_id" : NumberLong("20211028222550"), "last_scraped" : "2021-10-29", "name" : "a lovely place, top location", "description" : "Very central location,...", "neighborhood_overview" : "We live in one of the top locations of Zürich...", "picture_url" : "https://a0.muscache.com/pictures/7d41e016-e818-4fe1-9d42-a5d0ae34bdda.jpg", "host_id" : 854016, "host_url" : "https://www.airbnb.com/users/show/854016", "host_name" : "Delphine", "host_since" : "2011-07-22", "host_location" : "Zurich, Zurich, Switzerland", "host_about" : "I am a quiet, friendly and caring person\nI love Creativity, Painting, Writing, Reading, Music, Dancing, Yoga, Fashion and Decoration\nI travel since ever and mostly for my job all over the world", "host_response_time" : "within a day", "host_response_rate" : "100%", "host_acceptance_rate" : "0%", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_x_medium", "host_listings_count" : 1, "host_total_listings_count" : 1, "host_verifications" : "['email', 'phone', 'reviews']", "host_has_profile_pic" : "t", "host_identity_verified" : "f", "neighbourhood" : "Zurich, Switzerland", "neighbourhood_cleansed" : "Enge", "neighbourhood_group_cleansed" : "Kreis 2", "latitude" : 47.36565, "longitude" : 8.52753, "property_type" : "Private room in rental unit", "room_type" : "Private room", "accommodates" : 1, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Wifi\", \"Lock on bedroom door\", \"Heating\", \"Hangers\", \"Lake access\", \"Long term stays allowed\", \"Hair dryer\", \"Dryer\", \"Shampoo\", \"Washer\", \"Kitchen\", \"Elevator\"]", "price" : "$60.00", "minimum_nights" : 5, "maximum_nights" : 31, "minimum_minimum_nights" : 5, "maximum_minimum_nights" : 5, "minimum_maximum_nights" : 31, "maximum_maximum_nights" : 31, "minimum_nights_avg_ntm" : 5, "maximum_nights_avg_ntm" : 31, "has_availability" : "t", "availability_30" : 0, "availability_60" : 0, "availability_90" : 0, "availability_365" : 0, "calendar_last_scraped" : "2021-10-29", "number_of_reviews" : 9, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "2016-03-17", "last_review" : "2016-05-10", "review_scores_rating" : 4.89, "review_scores_accuracy" : 4.89, "review_scores_cleanliness" : 4.89, "review_scores_checkin" : 4.89, "review_scores_communication" : 4.89, "review_scores_location" : 5, "review_scores_value" : 4.89, "instant_bookable" : "f", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 0, "calculated_host_listings_count_private_rooms" : 1, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.13 }
```
<!-- | _id | id | listing_url | scrape_id | last_scraped | name | description | neighborhood_overview | picture_url | host_id | host_url | host_name | host_since | host_location | host_about | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url | host_picture_url | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type | room_type | accommodates | bathrooms_text | bedrooms | beds | amenities | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| ObjectId("6194703d051c47f3e6883fda") | 86645 | https://www.airbnb.com/rooms/86645 | NumberLong("20211028222550") | 2021-10-28 | Stadium Letzigrund - by Airhome | Discover a... | Located 300 meters... | https://a0.muscache.com/pictures/miso/Hosting-86645/original/d53da3fe-33c5-4b76-91ad-1a6797e4328e.jpeg | 475053 | https://www.airbnb.com/users/show/475053 | James | 2011-03-31 | Wherever you need me. Always happy to help. | Backed by... | within an hour | 99% | 93% | t | https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_x_medium | 36 | 36 | ['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id', 'work_email'] | t | t | Zurich, Switzerland | Sihlfeld | Kreis 3 | 47.38038 | 8.50461 | Entire rental unit | Entire home/apt | 3 | 1 bath | 1 | 2 | ["Air conditioning", ...] | 1 | 9999 | 1 | 1 | 9999 | 9999 | 1 | 9999 | t | 0 | 0 | 0 | 0 | 2021-10-28 | 50 | 1 | 0 | 2013-11-17 | 2021-07-16 | 4.52 | 4.67 | 4.7 | 4.64 | 4.77 | 4.6 | 4.47 | t | 18 | 18 | 0 | 0 | 0.52 |
| ObjectId("6194703d051c47f3e6883fdb") | 178448 | https://www.airbnb.com/rooms/178448 | NumberLong("20211028222550") | 2021-10-29 | a lovely place, top location | Very central location,... | We live in one of the... | https://a0.muscache.com/pictures/7d41e016-e818-4fe1-9d42-a5d0ae34bdda.jpg | 854016 | https://www.airbnb.com/users/show/854016 | Delphine | 2011-07-22 | Zurich, Zurich, Switzerland | I am a quiet, friendly and caring person... | within a day | 100% | 0% | f | https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_x_medium | 1 | 1 | ['email', 'phone', 'reviews'] | t | f | Zurich, Switzerland | Enge | Kreis 2 | 47.36565 | 8.52753 | Private room in rental unit | Private room | 1 | 1 bath | 1 | 1 | ["Wifi",...] | $60.00 | 5 | 31 | 5 | 5 | 31 | 31 | 5 | 31 | t | 0 | 0 | 0 | 0 | 2021-10-29 | 9 | 0 | 0 | 2016-03-17 | 2016-05-10 | 4.89 | 4.89 | 4.89 | 4.89 | 4.89 | 5 | 4.89 | f | 1 | 0 | 1 | 0 | 0.13 | -->
### 2) show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
```
db.listings.find().limit(10).sort({'id': 1}).pretty()
```
Output(only display the first 3 document output):
```
{
	"_id" : ObjectId("6194703d051c47f3e6883fda"),
	"id" : 86645,
	"listing_url" : "https://www.airbnb.com/rooms/86645",
	"scrape_id" : NumberLong("20211028222550"),
	"last_scraped" : "2021-10-28",
	"name" : "Stadium Letzigrund - by Airhome",
	"description" : "Discover a boutique apartment...",
	"neighborhood_overview" : "Located 300 meters to Zurich Letzigrund Stadion...",
	"picture_url" : "https://a0.muscache.com/pictures/miso/Hosting-86645/original/d53da3fe-33c5-4b76-91ad-1a6797e4328e.jpeg",
	"host_id" : 475053,
	"host_url" : "https://www.airbnb.com/users/show/475053",
	"host_name" : "James",
	"host_since" : "2011-03-31",
	"host_location" : "Wherever you need me. Always happy to help.",
	"host_about" : "Backed by an international team of guest support specialists and AI technology, James will be available for you 7/24 and always happy to help and assist you with your requests.",
	"host_response_time" : "within an hour",
	"host_response_rate" : "99%",
	"host_acceptance_rate" : "93%",
	"host_is_superhost" : "t",
	"host_thumbnail_url" : "https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/users/475053/profile_pic/1361399429/original.jpg?aki_policy=profile_x_medium",
	"host_listings_count" : 36,
	"host_total_listings_count" : 36,
	"host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id', 'work_email']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Zurich, Switzerland",
	"neighbourhood_cleansed" : "Sihlfeld",
	"neighbourhood_group_cleansed" : "Kreis 3",
	"latitude" : 47.38038,
	"longitude" : 8.50461,
	"property_type" : "Entire rental unit",
	"room_type" : "Entire home/apt",
	"accommodates" : 3,
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 2,
	"amenities" : "[\"Air conditioning\",...]",
	"price" : "$180.00",
	"minimum_nights" : 1,
	"maximum_nights" : 9999,
	"minimum_minimum_nights" : 1,
	"maximum_minimum_nights" : 1,
	"minimum_maximum_nights" : 9999,
	"maximum_maximum_nights" : 9999,
	"minimum_nights_avg_ntm" : 1,
	"maximum_nights_avg_ntm" : 9999,
	"has_availability" : "t",
	"availability_30" : 0,
	"availability_60" : 0,
	"availability_90" : 0,
	"availability_365" : 0,
	"calendar_last_scraped" : "2021-10-28",
	"number_of_reviews" : 50,
	"number_of_reviews_ltm" : 1,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2013-11-17",
	"last_review" : "2021-07-16",
	"review_scores_rating" : 4.52,
	"review_scores_accuracy" : 4.67,
	"review_scores_cleanliness" : 4.7,
	"review_scores_checkin" : 4.64,
	"review_scores_communication" : 4.77,
	"review_scores_location" : 4.6,
	"review_scores_value" : 4.47,
	"instant_bookable" : "t",
	"calculated_host_listings_count" : 18,
	"calculated_host_listings_count_entire_homes" : 18,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 0.52
}
{
	"_id" : ObjectId("6194703d051c47f3e6883fdb"),
	"id" : 178448,
	"listing_url" : "https://www.airbnb.com/rooms/178448",
	"scrape_id" : NumberLong("20211028222550"),
	"last_scraped" : "2021-10-29",
	"name" : "a lovely place, top location",
	"description" : "Very central location,...",
	"neighborhood_overview" : "We live in one of the top locations of Zürich, the Hürrlimann Areal where the headquarter of Google Europe is located <br />Its a 5 Minutes walk to Bahnhof Enge, 10 Minutes walk to the Bahnhofstrasse, 10 minutes to the lakeside.",
	"picture_url" : "https://a0.muscache.com/pictures/7d41e016-e818-4fe1-9d42-a5d0ae34bdda.jpg",
	"host_id" : 854016,
	"host_url" : "https://www.airbnb.com/users/show/854016",
	"host_name" : "Delphine",
	"host_since" : "2011-07-22",
	"host_location" : "Zurich, Zurich, Switzerland",
	"host_about" : "I am a quiet, friendly and caring person...",
	"host_response_time" : "within a day",
	"host_response_rate" : "100%",
	"host_acceptance_rate" : "0%",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/users/854016/profile_pic/1311363294/original.jpg?aki_policy=profile_x_medium",
	"host_listings_count" : 1,
	"host_total_listings_count" : 1,
	"host_verifications" : "['email', 'phone', 'reviews']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "f",
	"neighbourhood" : "Zurich, Switzerland",
	"neighbourhood_cleansed" : "Enge",
	"neighbourhood_group_cleansed" : "Kreis 2",
	"latitude" : 47.36565,
	"longitude" : 8.52753,
	"property_type" : "Private room in rental unit",
	"room_type" : "Private room",
	"accommodates" : 1,
	"bathrooms_text" : "1 bath",
	"bedrooms" : 1,
	"beds" : 1,
	"amenities" : "[\"Wifi\",...]",
	"price" : "$60.00",
	"minimum_nights" : 5,
	"maximum_nights" : 31,
	"minimum_minimum_nights" : 5,
	"maximum_minimum_nights" : 5,
	"minimum_maximum_nights" : 31,
	"maximum_maximum_nights" : 31,
	"minimum_nights_avg_ntm" : 5,
	"maximum_nights_avg_ntm" : 31,
	"has_availability" : "t",
	"availability_30" : 0,
	"availability_60" : 0,
	"availability_90" : 0,
	"availability_365" : 0,
	"calendar_last_scraped" : "2021-10-29",
	"number_of_reviews" : 9,
	"number_of_reviews_ltm" : 0,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2016-03-17",
	"last_review" : "2016-05-10",
	"review_scores_rating" : 4.89,
	"review_scores_accuracy" : 4.89,
	"review_scores_cleanliness" : 4.89,
	"review_scores_checkin" : 4.89,
	"review_scores_communication" : 4.89,
	"review_scores_location" : 5,
	"review_scores_value" : 4.89,
	"instant_bookable" : "f",
	"calculated_host_listings_count" : 1,
	"calculated_host_listings_count_entire_homes" : 0,
	"calculated_host_listings_count_private_rooms" : 1,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 0.13
}
{
	"_id" : ObjectId("6194703d051c47f3e6883fdc"),
	"id" : 227039,
	"listing_url" : "https://www.airbnb.com/rooms/227039",
	"scrape_id" : NumberLong("20211028222550"),
	"last_scraped" : "2021-10-28",
	"name" : "*Luxury Penthouse in the heart of trendy Zurich*",
	"description" : "Modern and unique penthouse apartment...",
	"neighborhood_overview" : "Zurich is hip-circuit with the Swiss peacefulness!...",
	"picture_url" : "https://a0.muscache.com/pictures/28325669/6d4b0af4_original.jpg",
	"host_id" : 1184427,
	"host_url" : "https://www.airbnb.com/users/show/1184427",
	"host_name" : "Lucas",
	"host_since" : "2011-09-20",
	"host_location" : "Zürich, Zurich, Switzerland",
	"host_about" : "I'm a Swiss management consultant...",
	"host_response_time" : "within a day",
	"host_response_rate" : "100%",
	"host_acceptance_rate" : "20%",
	"host_is_superhost" : "f",
	"host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/23d284a1-b4ac-4e64-b894-9d4d2a50af66.jpg?aki_policy=profile_small",
	"host_picture_url" : "https://a0.muscache.com/im/pictures/user/23d284a1-b4ac-4e64-b894-9d4d2a50af66.jpg?aki_policy=profile_x_medium",
	"host_listings_count" : 2,
	"host_total_listings_count" : 2,
	"host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'offline_government_id', 'selfie', 'government_id', 'identity_manual', 'work_email']",
	"host_has_profile_pic" : "t",
	"host_identity_verified" : "t",
	"neighbourhood" : "Zurich, Canton of Zurich, Switzerland",
	"neighbourhood_cleansed" : "Escher Wyss",
	"neighbourhood_group_cleansed" : "Kreis 5",
	"latitude" : 47.38942,
	"longitude" : 8.51881,
	"property_type" : "Entire condominium (condo)",
	"room_type" : "Entire home/apt",
	"accommodates" : 3,
	"bathrooms_text" : "1.5 baths",
	"bedrooms" : 2,
	"beds" : 2,
	"amenities" : "[\"Outdoor furniture\",...]",
	"price" : "$400.00",
	"minimum_nights" : 4,
	"maximum_nights" : 14,
	"minimum_minimum_nights" : 4,
	"maximum_minimum_nights" : 4,
	"minimum_maximum_nights" : 14,
	"maximum_maximum_nights" : 14,
	"minimum_nights_avg_ntm" : 4,
	"maximum_nights_avg_ntm" : 14,
	"has_availability" : "t",
	"availability_30" : 23,
	"availability_60" : 53,
	"availability_90" : 83,
	"availability_365" : 358,
	"calendar_last_scraped" : "2021-10-28",
	"number_of_reviews" : 28,
	"number_of_reviews_ltm" : 1,
	"number_of_reviews_l30d" : 0,
	"first_review" : "2014-08-18",
	"last_review" : "2019-12-20",
	"review_scores_rating" : 4.96,
	"review_scores_accuracy" : 5,
	"review_scores_cleanliness" : 4.93,
	"review_scores_checkin" : 4.96,
	"review_scores_communication" : 4.93,
	"review_scores_location" : 4.93,
	"review_scores_value" : 4.86,
	"instant_bookable" : "f",
	"calculated_host_listings_count" : 1,
	"calculated_host_listings_count_entire_homes" : 1,
	"calculated_host_listings_count_private_rooms" : 0,
	"calculated_host_listings_count_shared_rooms" : 0,
	"reviews_per_month" : 0.32
}

```
### 3) choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts(only show the name, price, neighbourhood, host_name, and host_is_superhost for each result)
The following `aggregate()` rule first finds all documents that have "host_is_superhost" = "t", and then groups these documents by "host_id". For a clearer demonstration on the feasibility, I added extra pipeline var `host_count` to record the number of listings of each host, and then get the two host that owns the most listings by `{$limit: 2}`.
```
db.listings.aggregate([
    {$match: {"host_is_superhost": "t"}},
    {$group: { _id:"$host_id",host_count:{$sum:1},listingOfHost:{
        $push:{
            name:"$name",
            price:"$price",
            neighbourhood:"$neighbourhood",
            host_name:"$host_name",
            host_is_superhost:"$host_is_superhost"
        }}}
    },
    {$sort: {"host_count":-1}},
    {$limit: 2},
]).pretty()
```
The result is the following:
```
{
	"_id" : 19610180,
	"host_count" : 6,
	"listingOfHost" : [
		{
			"name" : "Stadt Zürich Guesthouse (Zimmer3)",
			"price" : "$45.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Stadt Zürich 3, Appartement-Studio (3)",
			"price" : "$74.00",
			"neighbourhood" : "Zurich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Stadt Zürich 4101-Appartement Albisriederplatz",
			"price" : "$75.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Stadt Zürich 206 -Studio nähe Albisriederplatz(6)",
			"price" : "$85.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Stadt Zürich  4102 Kleines Studio Albisriederplatz",
			"price" : "$67.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Stadt Zürich 4401-Appartement  Albisriederplatz",
			"price" : "$85.00",
			"neighbourhood" : "Zürich, Zurich, Switzerland",
			"host_name" : "Rossana",
			"host_is_superhost" : "t"
		}
	]
}
{
	"_id" : 23561865,
	"host_count" : 5,
	"listingOfHost" : [
		{
			"name" : "Charming 2BR apartment/old town UZ6",
			"price" : "$179.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Tania",
			"host_is_superhost" : "t"
		},
		{
			"name" : "1BR flat in middle old town (RDN)",
			"price" : "$159.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Tania",
			"host_is_superhost" : "t"
		},
		{
			"name" : "2 BR apartment near the lake / city centre D5",
			"price" : "$169.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Tania",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Fantastic 1 BR flat / city center (Fröhlich 1)",
			"price" : "$159.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Tania",
			"host_is_superhost" : "t"
		},
		{
			"name" : "Amazing flat with 4 balconies/city center (West2)",
			"price" : "$119.00",
			"neighbourhood" : "Zürich, Switzerland",
			"host_name" : "Tania",
			"host_is_superhost" : "t"
		}
	]
}

```
### 4) find all the unique host_name values
Use `distinct()` to get all unique values appeared in the collection:
```
db.listings.distinct("host_name")
```
which gives out the names in a list(output is clipped for easier display):
```
[
	"Alberto",
	"Aleksandra",
	"Alexandra",
	"Amandine",
	"Andrea",
	...
    ...
    ...
	"Thomas M.",
	"Trix",
	"Violetta",
	"Visakha",
	"Yvonne",
	"Zurichhome"
]
```
### 5) find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending(only show the name, beds, review_scores_rating, and price)
Use `find` with querys joined by AND logic that a place must be in Zurich, Canton of Zurich, Switzerland neighbourhood and has more than 2 beds (`"beds":{$gt: 2}`), and turn on name, beds, review_scores_rating, and price in the projection, then sort by review_scores_rating, descending:
```
db.listings.find(
    { 
        "neighbourhood": "Zurich, Canton of Zurich, Switzerland",
        "beds":{$gt: 2},
    },
    {
        "name": 1,
        "beds": 1,
        "review_scores_rating": 1,
        "price": 1
    }
).sort({"review_scores_rating":-1})
```
The output is:
```
{ "_id" : ObjectId("6194703d051c47f3e6883fe7"), "name" : "Grosse charmante Wohnung nähe Oper", "beds" : 3, "price" : "$379.00", "review_scores_rating" : 4.96 }
{ "_id" : ObjectId("6194703d051c47f3e6883fe2"), "name" : "bright and great duplex in the heart of Zurich", "beds" : 7, "price" : "$65.00", "review_scores_rating" : 4.86 }
{ "_id" : ObjectId("6194703d051c47f3e6883fe1"), "name" : "Duplex  Flat, 120 m2 7-8  persons", "beds" : 6, "price" : "$213.00", "review_scores_rating" : 4.67 }
```

### 6) show the number of listings per host
Use similar logic as Q3, first group by "host_id" and find the number of this host's listings by `{$sum:1}`. I did something extra to sort it in descending order of counts:
```
db.listings.aggregate([
    {$group: { _id:"$host_id",host_count:{$sum:1}}},
    {$sort: {"host_count":-1}},
])
```
and the first few results are like (note "_id" is the "host_id"):
```
{ "_id" : 12886487, "host_count" : 34 }
{ "_id" : 3528377, "host_count" : 15 }
{ "_id" : 19610180, "host_count" : 6 }
{ "_id" : 475053, "host_count" : 5 }
{ "_id" : 23561865, "host_count" : 5 }
{ "_id" : 16506657, "host_count" : 4 }
{ "_id" : 134482609, "host_count" : 4 }
{ "_id" : 83271512, "host_count" : 4 }
...
```

### 7) find the average review_scores_rating per neighborhood, and only show the ones above a 95, sorted in descending order of rating
My data has review_scores_rating as value out of 5. To convert it into a out-of-100-point counting, use logic $avg/5 * 100 > 95.
```
db.listings.aggregate([
    {$group: { _id:"$neighbourhood",average_rating:{$avg:"$review_scores_rating"}}},
    {$match: {"average_rating": {$gt : 95/100*5}}},
    {$sort: {"average_rating":-1}},
])
```
The result is:
```
{ "_id" : "Zurich, Zürich, Switzerland", "average_rating" : 4.92 }
{ "_id" : "Switzerland", "average_rating" : 4.9 }
{ "_id" : "Zurich, Canton of Zurich, Switzerland", "average_rating" : 4.884166666666666 }
{ "_id" : "Zürich, ZH, Switzerland", "average_rating" : 4.817777777777779 }
{ "_id" : "Zürich, Switzerland", "average_rating" : 4.780673758865248 }
```

