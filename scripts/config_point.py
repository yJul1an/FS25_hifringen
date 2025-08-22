
layers = [
    ("Overview_bbox", 1081695.7141830747, 1093943.323190762, 6094538.707886295, 6106786.319813694),
    ("Overview_bbox_with_margin", 1081195, 1094443, 6094038, 6107286)
]
for layer in layers:
    name = "Points_" + layer[0]
    north, south, east, west = layer[1:]

    top_left = QgsPointXY(north, west)
    top_right = QgsPointXY(north, east)
    bottom_right = QgsPointXY(south, east)
    bottom_left = QgsPointXY(south, west)

    points = [top_left, top_right, bottom_right, bottom_left, top_left]

    # Create a new layer
    layer = QgsVectorLayer('Point?crs=EPSG:3857', name, 'memory')
    provider = layer.dataProvider()

    # Add fields
    provider.addAttributes([QgsField("id", QVariant.Int)])
    layer.updateFields()

    # Create and add features for each point
    for i, point in enumerate(points):
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        feature.setAttributes([i + 1])
        provider.addFeature(feature)

    layer.updateExtents()

    # Add the layer to the project
    QgsProject.instance().addMapLayer(layer)
