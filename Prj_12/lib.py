import requests

class Geoserver:
    def __init__(self, url, user, passw):
        self.url = url
        self.username = user
        self.password = passw

    def get_workspaces(self):

        # GeoServer REST API endpoint for workspaces
        url = self.url + "geoserver/rest/workspaces"

        # Send a GET request to retrieve the list of workspaces
        response = requests.get(url, auth=(self.username, self.password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the list of workspaces
            if response.json()["workspaces"]:
                workspaces = response.json()["workspaces"]["workspace"]
                workspaces_list = [workspace["name"] for workspace in workspaces]
                return workspaces_list
            return []
        else:
            raise ConnectionError("Failed to retrieve workspaces. Status code: " + str(response.status_code))
        
    def get_datastores(self, workspace):

        url = self.url + "geoserver/rest/workspaces/" + workspace + "/datastores"

        response = requests.get(url, auth=(self.username, self.password))

        if response.status_code == 200:
            if response.json()["dataStores"]:
                datastores = response.json()["dataStores"]["dataStore"]
                datastores_list = [datastore["name"] for datastore in datastores]
                return datastores_list
            else:
                return []
        else:
            raise ConnectionError("Failed to retrieve datastores. Status code: " + str(response.status_code))
        
    def create_workspace(self, name):
        if name in self.get_workspaces():
            raise KeyError(f"There is a workspace with this name. -({name})-")

        # GeoServer REST API endpoint for workspaces
        url = self.url + "geoserver/rest/workspaces"

        # XML payload for creating a new workspace
        xml_data = "<workspace><name>" + name + "</name></workspace>"

        # Request headers
        headers = {
            "Content-type": "text/xml",
        }

        # Send a POST request to create a new workspace
        response = requests.post(url, auth=(self.username, self.password), headers=headers, data=xml_data)

        # Check if the request was successful (status code 201 for Created)
        if response.status_code == 201:
            print("Workspace created successfully.")
        else:
            print("Failed to create workspace. Status code:", response.status_code)

    def create_datastore_shapefile(self, workspace, datastore, shapefile_path):
        if datastore in self.get_datastores(workspace):
            raise KeyError(f"There is a datastore with this name. -({datastore})-")

        # GeoServer REST API endpoint for uploading shapefile
        url = self.url + "geoserver/rest/workspaces/" + workspace + "/datastores/" + datastore + "/" + "file.shp"

        print(url)

        # Request headers
        headers = {
            "Content-type": "application/zip",
        }

        # Read the shapefile data
        with open(shapefile_path, "rb") as file:
            # shapefile_data = file.read()
            response = requests.put(url, data=file, auth=('admin', 'geoserver'), headers=headers)

        # # Send a PUT request to upload the shapefile
        # response = requests.put(url, auth=(self.username, self.password), headers=headers, data=shapefile_data)


        # Check if the request was successful (status code 201 for Created)
        if response.status_code == 201:
            print("Shapefile uploaded successfully.")
        else:
            print("Failed to upload shapefile. Status code:", response.status_code)


