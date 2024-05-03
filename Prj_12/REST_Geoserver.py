import os

from lib import Geoserver

my_geoserver = Geoserver("http://localhost:8080/", "admin", "geoserver")

new_workspace = "test_REST"

my_geoserver.create_workspace(new_workspace)

# print(my_geoserver.get_datastores("rasht"))

new_datastore = "Australia_railways"
zip_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "AUS_rrd.zip")


# print(my_geoserver.get_datastores("rasht"))


my_geoserver.create_datastore_shapefile(new_workspace, new_datastore, zip_file_path)



