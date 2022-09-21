import pandas as pd
import pylab as pl
from IPython import embed

trips = pd.read_csv("../data/bysykkel/trips-2021.9.1-2021.9.30.csv")
station_data = trips.groupby(['start_station_id', 'start_station_longitude', 
                    'start_station_latitude', 'start_station_name']).count()
station_data = station_data.reset_index()
station_data = station_data.drop(columns=station_data.columns[-7:])
station_data = station_data.rename(columns={'started_at':'started_trips'})
station_data = station_data.set_index('start_station_id')
station_data['ended_trips'] = trips['end_station_id'].value_counts()

from ipywidgets import HTML
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles, Circle, Polyline
oslo_center = 59.9127, 10.7461    #NB ipyleaflet uses Lat-Long (i.e. y,x, when specifying coordinates)
oslo_map = Map(center=oslo_center, zoom=13)
def add_markers(row):
    center = row['start_station_latitude'], row['start_station_longitude']
    marker = Circle(location=center, radius=int(0.04*row["started_trips"]), color = 'green')
    oslo_map.add_layer(marker)
    



#station_data.apply(add_markers, axis=1)


new_trips_data = trips[trips['start_station_name'] == 'Stensgata']

end_stations = new_trips_data['end_station_id'].value_counts()
new_stations_data = station_data[station_data['start_station_name'] == 'Stensgata']

start_pos = float(new_stations_data['start_station_latitude']), float(new_stations_data['start_station_longitude'])

def add_lines(row):
    start = start_pos
    end = row['end_station_latitude'], row['end_station_longitude']
    circle = Circle(location=end, color='red', radius=int(5*(end_stations[row['end_station_id']])))
    circle_start = Circle(location=start, color='green', radius=10)
    oslo_map.add_layer(circle)
    oslo_map.add_layer(circle_start)
    circle.popup = HTML(f"{row['end_station_name']} <br> Trips ended: {end_stations[row['end_station_id']]}")

new_trips_data.apply(add_lines, axis=1)
oslo_map.save('oslo_map.html')

