    from bigml.api import BigML
    api = BigML()

    source1 = api.create_source("iris.csv")
    api.ok(source1)

    dataset1 = api.create_dataset(source1, \
        {'name': 'iris dataset'})
    api.ok(dataset1)

    cluster1 = api.create_cluster(dataset1, \
        {'name': "iris dataset's cluster"})
    api.ok(cluster1)

    batchcentroid1 = api.create_batch_centroid(cluster1, dataset1, \
        {'name': "Batch Centroid of iris dataset's cluster with iris dataset",
         'output_dataset': True})
    api.ok(batchcentroid1)

    dataset2 = api.get_dataset(batchcentroid1['object']['output_dataset_resource'])
    api.ok(dataset2)

    dataset2 = api.update_dataset(dataset2, \
        {'fields': {'000000': {'name': 'cluster'}},
         'name': 'iris dataset - batchcentroid'})
    api.ok(dataset2)

    dataset3 = api.create_dataset(dataset2, \
        {'input_fields': ['000000'],
         'name': 'my_dataset_from_dataset_from_batch_centroid_name',
         'new_fields': [{'field': '( integer ( replace ( field "cluster" ) '
                                  '"Cluster " "" ) )',
                         'name': 'Cluster'}]})
    api.ok(dataset3)
