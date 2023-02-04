class PipelineHelper:
    @staticmethod
    def project(field_mapping):
        return {"$project": field_mapping}

    @staticmethod
    def match(criteria):
        return {"$match": criteria}

    @staticmethod
    def group(grouping, calculated_fields):
        return {"$group": {**grouping, **calculated_fields}}

    @staticmethod
    def sort(sort_order):
        return {"$sort": sort_order}

    @staticmethod
    def skip(skip_count):
        return {"$skip": skip_count}

    @staticmethod
    def limit(limit_count):
        return {"$limit": limit_count}

    @staticmethod
    def first():
        return {"$first": "$$ROOT"}

    @staticmethod
    def last():
        return {"$last": "$$ROOT"}

    @staticmethod
    def unwind(field):
        return {"$unwind": field}
