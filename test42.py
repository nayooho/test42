from glob import glob
import numpy as np
import folium
import  pandas as pd
from folium import plugins
import pymongo.database
from folium.plugins import HeatMap
import json

import requests

url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
data = json.loads(requests.get(f"{url}/vis1.json").text)
print("ข้อมูล .json ในเว็บ")
print(data)

my_map42 = folium.Map([7.30161,100.16535], tiles='Stamen Terrain', zoom_start=6)
marker = folium.Marker(
    location=[7.218871184761596, 100.624819877497147],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(data, width=450, height=250) #น่าจะวนลูป data ต่างๆ ที่บันทึกใน Datafram เช่น jason excel
    ),
)
marker.add_to(my_map42)



with open('Graph.json') as f:
    json_data = json.load(f)
    print("ข้อมูล Graph.json ในเครื่อง")
    print(json_data)


marker2 = folium.Marker(
    location=[7.305871184761596, 100.169819877497147],
    popup=folium.Popup(max_width=450).add_child(folium.Vega(json_data, width=450, height=250)),
)
marker2.add_to(my_map42)

with open('Graph2.json') as f:
    json_data = json.load(f)
    print("ข้อมูล Graph2.json ในเครื่อง")
    print(json_data)

for i in json_data:
    print(i)

marker3 = folium.Marker(
    location=[7.395871184761596, 100.279819877497147],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json_data, width=450, height=250)
    ),
)
marker3.add_to(my_map42)


#my_map42 = folium.Map([7.30161,100.16535], tiles='Stamen Terrain', zoom_start=6)



# Add custom base maps to folium
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}
# Add custom basemaps
basemaps['Google Maps'].add_to(my_map42)
basemaps['Google Satellite Hybrid'].add_to(my_map42)
# basemaps['Esri Satellite'].add_to(my_map21)
#basemaps['durian'].add_to(my_map21)
#basemaps['homesick'].add_to(my_map21)

# fullscreen
plugins.Fullscreen().add_to(my_map42)

# GPS
plugins.LocateControl().add_to(my_map42)

# mouse position
fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",
                      lng_formatter=fmtr,lat_formatter=fmtr).add_to(my_map42)


# Add the draw
plugins.Draw(export=True, filename='data.json', position='topleft', draw_options=None, edit_options=None).add_to(
    my_map42)

# Add measure tool
plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles',
                       primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(my_map42)



#lon, lat = -86.276, 30.935
#zoom_start = 5

"""
data = (
    np.random.normal(size=(100, 3)) *
    np.array([[1, 1, 1]]) +
    np.array([[48, 5, 1]])
).tolist()
my_map42 = folium.Map([48, 5], tiles='stamentoner', zoom_start=6)
print(data)

for i in data :
    print(i)

HeatMap(data).add_to(folium.FeatureGroup(name='Heat Map').add_to(my_map42))
folium.LayerControl().add_to(my_map42)

"""

data2 = ([7.30161,100.165352],[7.300614,100.165631],[7.300689,100.166624],[7.301679,100.166484,])
data3 = ([7.40161,100.265352],[7.300614,100.165631],[7.200689,100.256624],[7.301679,100.246484,])
dataframe3 = pd.DataFrame(data3).to_string
print(dataframe3)

data4 = pd.read_excel("Plot_test3.xlsx")
data4 = data4[['X','Y']]
data4 = pd.DataFrame(data4)
products_list = data4.values.tolist()
print(data4)
print(products_list)
data4 = products_list



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["my_abt"]
mycol = mydb["employer"]
cursor = mycol.find()
entries = list(cursor)
# entries[:5]

data8 = pd.DataFrame(entries, dtype=str)
data8.head(3)
print(data8)
data8 = data8[['Lat','Lon']]
print(data8)
data8 = data8.values.tolist()
print(data8)
for i in data8 :
    print(i)
data8 = pd.DataFrame(data8)
print(data8)



data9 = pd.read_excel("Plot_test4.xlsx")
data10 = data9[['XY','P_NAME1']]
data9 = pd.DataFrame(data9)
print(data9)

#data9=data9['X'].str.split(',', expand=True)
#print(data9)
data11=data9[['X', 'Y']] = data9['XY'].str.split(',', expand=True)
print(data11)
print(data9)
dt = data11.join(data9)
#print(dt)
data15 = data9[['X','Y','P_NAME1']]
print(data15)

for i in range(0, len(data15)):
    folium.Marker(
        location=[data15.iloc[i]['X'], data15.iloc[i]['Y']],
        popup=data15.iloc[i]['P_NAME1'],
        tooltip=data15.iloc[i]['P_NAME1'],
        
    ).add_to(my_map42)


col_one_list = dt['XY'].tolist()
col_one_arr = dt['XY'].to_numpy()
print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")
print(f"\ncol_one_arr:\n{col_one_arr}\ntype:{type(col_one_arr)}")

for i in col_one_list:
    print([i])

for i in col_one_arr:
    print([i],[i])

list_to_Dataframe = pd.DataFrame(col_one_list)
print(list_to_Dataframe)

data_dict = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
             'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data_dict)

print(f"DataFrame:\n{df}\n")
print(f"column types:\n{df.dtypes}")

col_one_list = df['one'].tolist()

col_one_arr = df['one'].to_numpy()

print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")
print(f"\ncol_one_arr:\n{col_one_arr}\ntype:{type(col_one_arr)}")


array = ['first', 'sentence', 'step', 'second', 'sentence', 'step', 'third', 'step', 'some', 'other', 'sentence']

def split_list(lst, sep):
    return [i.split() for i in ' '.join(lst).split(sep)]
print(split_list(array, 'step'))


array=['7,10','7,11','7,12','7,13','7,14']
newlist1 = []
for i in array:
     newlist1.append([i])

print(newlist1) #[['7,10'], ['7,11'], ['7,12'], ['7,13'], ['7,14']]


sa_df = pd.DataFrame({
    "name":["Al_riyad","Makkah","Aseer","Al_madinah","Eastern_region","Northern_borders","Al_bahah","Najran","Jazan","Al_qaseeem","Hail","Al_jawf","Tabuk"],
    "latitude":[23.05,21.389082,19.15,24.9,24.0,30.25,20.16667,18.41667,17.33333,27.08333,27.4,30.05,28.25],
    "longitude":[45.55,39.857910,42.95,39.5,49.75,42.41667,41.43333,46.91667,42.66667,43.46667,41.45,39.6,37.16667],
    "images":["alriyad.png","makkah.png","aseer.png","madina.png","eastern_region.png","northern_borders.png","albahah.png","najran.png","jazan.png","alqaseem.png","hail.png","aljawf.png","tabuk.png"],
    "population":["8,216,284","8,557,766","2,211,875","1,423,935","4,900,325","365,231","476,172","582,243","1,567,547","1,423,935","699,774","508,475","910,030"],
#    "dfs_deaths":[alriyad["deaths"].sum(), makkah["deaths"].sum(), aseer["deaths"].sum(), madina["deaths"].sum(), eastern_region["deaths"].sum(), northern_borders["deaths"].sum(), albahah["deaths"].sum(), najran["deaths"].sum(), jazan["deaths"].sum(), alqaseem["deaths"].sum(), hail["deaths"].sum(), aljawf["deaths"].sum(), tabuk["deaths"].sum()],
#    "dfs_recovories":[alriyad["recovories"].sum(), makkah["recovories"].sum(), aseer["recovories"].sum(), madina["recovories"].sum(), eastern_region["recovories"].sum(), northern_borders["recovories"].sum(), albahah["recovories"].sum(), najran["recovories"].sum(), jazan["recovories"].sum(), alqaseem["recovories"].sum(), hail["recovories"].sum(), aljawf["recovories"].sum(), tabuk["recovories"].sum()],
#    "dfs_cases":[alriyad["cases"].sum(), makkah["cases"].sum(), aseer["cases"].sum(), madina["cases"].sum(), eastern_region["cases"].sum(), northern_borders["cases"].sum(), albahah["cases"].sum(), najran["cases"].sum(), jazan["cases"].sum(), alqaseem["cases"].sum(), hail["cases"].sum(), aljawf["cases"].sum(), tabuk["cases"].sum()]
})
print(sa_df)
lat = list(sa_df["latitude"])
lon = list(sa_df["longitude"])
name = list(sa_df["name"])
image = list(sa_df["images"])
population = list(sa_df["population"])
#deaths = list(sa_df["dfs_deaths"])
#recovories = list(sa_df["dfs_recovories"])
#cases = list(sa_df["dfs_cases"])


fg = folium.FeatureGroup(name="My Map").add_to(my_map42)

for lt,ln,nm,img,ppl in zip(lat, lon, name, image, population):
    html = f'''
        <p>region: {nm}<p/>
        <p>population: {ppl}<p/>
        <p>date: feb_2021</p>
        <img src="{img}">'''
    iframe = folium.IFrame(html, width=300, height=400)
    popup = folium.Popup(iframe , max_width=400)
    marker = folium.Marker([lt,ln], popup=(popup), tooltip="click for covid-19 info").add_to(my_map42)
    my_map42.add_child(marker)

# Python3 code to demonstrate # converting list of strings to int # using naive method
# initializing list
test_list = ['7', '11', '12']
# Printing original list
print("Original list is : " + str(test_list))
# using naive method to
# perform conversion
for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])
# Printing modified list
print("Modified list is : " + str(test_list))


test = [[2, 3, 5, 6, 9, 10, 11, 13, 14, 16, 18, 20, 23, 24, 25], [1, 4, 5, 6, 7, 9, 11, 12, 13, 15, 16, 19, 20, 23, 24]] # there are hundreds of lists in the original list
list_num_sor = []
new_list = []
for row in test:
    for i in range(1, 26):
        if i in row:
            new_list.append('1')
        else:
            new_list.append('0')
    list_num_sor.append(new_list)
print(list_num_sor )
print(new_list )


# data8 = pd.read_geojason("data (18).geojson")
HeatMap(data3).add_to(folium.FeatureGroup(name='จุดน้ำท่วมขัง').add_to(my_map42))
HeatMap(data2).add_to(folium.FeatureGroup(name='จุดถนนชำรุด').add_to(my_map42))
HeatMap(data4).add_to(folium.FeatureGroup(name='ครอบครัวด้อยโอกาส').add_to(my_map42))
HeatMap(data8).add_to(folium.FeatureGroup(name='บ้านพนักงาน อบต.').add_to(my_map42))
#HeatMap(newlist1).add_to(folium.FeatureGroup(name='ทดสอบคอลัมไปลีส').add_to(my_map42))


# Add tiles
folium.TileLayer('stamentoner').add_to(my_map42)
folium.TileLayer('stamenwatercolor').add_to(my_map42)
#folium.TileLayer('Esri Satellite').add_to(my_map42)
folium.TileLayer('openstreetmap').add_to(my_map42)
# Add the option to switch tiles


folium.LayerControl().add_to(my_map42)
my_map42.save(" my_map42.html ")
