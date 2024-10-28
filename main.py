import folium
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Function to create and display the map with multiple locations
def create_map(locations):
    if len(locations) > 0:
        # Extract latitude and longitude from the locations
        lats = [lat for lat, lon, name in locations]
        lons = [lon for lat, lon, name in locations]

        # Calculate the bounds of the locations
        south = min(lats) - 0.1  # Adding a little padding
        north = max(lats) + 0.1
        west = min(lons) - 0.1
        east = max(lons) + 0.1

        # Create a map with bounds
        m = folium.Map(location=[(north + south) / 2, (west + east) / 2], zoom_start=7)

        # Add each location to the map
        for lat, lon, name in locations:
            if name == "Cork":
                # Add a red marker for Cork
                folium.Marker(location=[lat, lon], popup=name,
                              icon=folium.Icon(color='red')).add_to(m)
            else:
                # Add default markers for others
                folium.Marker(location=[lat, lon], popup=name).add_to(m)

        # Fit the map to the bounds of the locations
        m.fit_bounds([[south, west], [north, east]])

        # Save the map to an HTML file
        map_file = 'map.html'
        m.save(map_file)

        # Open the map in the default web browser
        webbrowser.open('file://' + os.path.realpath(map_file))

        # Convert the HTML file to PNG using Selenium
        options = webdriver.ChromeOptions()
        options.headless = True  # Run in headless mode
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Set the window size for higher resolution
        driver.set_window_size(1920, 1080)  # Set to desired resolution

        driver.get('file://' + os.path.realpath(map_file))

        # Save screenshot as PNG
        driver.save_screenshot('map.png')
        driver.quit()  # Close the browser

        print("Map saved as map.png")

    else:
        print("No locations provided.")

# Example list of locations (latitude, longitude, name)
locations = [
    (51.83043004878262, -8.33600007116382, "P20: Janssen Sciences"),     # Ringaskiddy
    (51.834372052850505, -8.345825526982917, "P19: Biomarin Shanbally"),       # Ringaskiddy
    (51.8337367910098, -8.341098928836182, "P18: Pfizer Ringaskiddy"),     # Ringaskiddy
    (51.89046234058519, -8.531085599999999, "P17: Stryker NeuroVascular Cork"),  # Cork
    (51.88997725576445, -8.527611286508538, "P16: Boston Scientific Cork"),  # Cork
    (51.88734162350156, -8.415103613491459, "P15: Jacobs"),  # Cork
    (51.91090731580473, -8.281761328836179, "P14: AbbVie Cork"),  # Cork
    (52.37364917635209, -7.7203269711638205, "P13: Abbott Ireland Vascular"),  # Tipperary
    (52.3722307818172, -7.72248934232764, "P12: Boston Scientific Clonmel"),  # Tipperary
    (52.36291376399661, -7.511826728836179, "P11: MSD Ballydine"),  # Tipperary
    (52.50353388913283, -7.890013157672361, "P10: Amneal"),  # Tipperary
    (52.36006453037894, -7.668827274565339, "P9 : AlbyPharma"),  # Tipperary
    (52.62026025222737, -8.66228625767236, "P8: Regeneron"),  # Limerick
    (52.6257662211696, -8.661893686508538, "P7: Stryker Orthopaedics"),  # Limerick
    (52.65177549922872, -8.599183000000002, "P6: Shannon MicroCoil"),  # Limerick
    (52.670583431345115, -8.53765445767236, "P5: Johnson & Johnson Vision Care"),  # Limerick
    (52.67445989221478, -8.55087901349146, "P4: Cook Medical, 52.67445989221478"),  # Limerick
    (52.673830072814916, -8.556541115344722, "P3: BD-RCI Limerick"),  # Limerick
    (52.66500730915583, -8.501162615344722, "P2: Teleflex Medical Ireland Limited"),  # Limerick
    (52.660832249756, -8.499307471163819, "P1: Serosep Ltd."),  # Limerick


]

# Create and display the map
create_map(locations)