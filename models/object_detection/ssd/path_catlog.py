import os


class DatasetCatalog:
    DATA_DIR = 'datasets'
    DATASETS = {
        'svhn_train':{
            "data_dir": "svhn_train",
            "ann_file": "annotations/train_coco.json"
        },
        'svhn_test':{
            "data_dir": "svhn_test",
            "ann_file": "annotations/test_coco.json"
        }
    }

    @staticmethod
    def get(name):
        if "voc" in name:
            voc_root = DatasetCatalog.DATA_DIR
            if 'VOC_ROOT' in os.environ:
                voc_root = os.environ['VOC_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(voc_root, attrs["data_dir"]),
                split=attrs["split"],
            )
            return dict(factory="VOCDataset", args=args)
        elif "coco" in name:
            coco_root = DatasetCatalog.DATA_DIR
            if 'COCO_ROOT' in os.environ:
                coco_root = os.environ['COCO_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(coco_root, attrs["data_dir"]),
                ann_file=os.path.join(coco_root, attrs["ann_file"]),
            )
            return dict(factory="COCODataset", args=args)
        elif "svhn" in name:
            svhn_root = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(svhn_root, attrs["data_dir"]),
                ann_file=os.path.join(svhn_root, attrs["ann_file"]),
            )
            return dict(factory="SVHNDataset", args=args)

        raise RuntimeError("Dataset not available: {}".format(name))
