import graphene
from graphene_django.types import DjangoObjectType
from .models import AnalyticsRecord

class AnalyticsRecordType(DjangoObjectType):
    class Meta:
        model = AnalyticsRecord
        fields = ('id', 'user', 'session', 'action', 'timestamp')

class Query(graphene.ObjectType):
    all_analytics_records = graphene.List(AnalyticsRecordType)
    analytics_record = graphene.Field(AnalyticsRecordType, id=graphene.Int())

    def resolve_all_analytics_records(self, info, **kwargs):
        # Assuming that the user has the permission to view analytics
        return AnalyticsRecord.objects.all()

    def resolve_analytics_record(self, info, id, **kwargs):
        # Assuming that the user has the permission to view this specific analytics record
        return AnalyticsRecord.objects.get(pk=id)

class CreateAnalyticsRecord(graphene.Mutation):
    class Arguments:
        user = graphene.Int(required=True)
        session = graphene.String(required=True)
        action = graphene.String(required=True)
        timestamp = graphene.DateTime(required=True)

    analytics_record = graphene.Field(AnalyticsRecordType)

    def mutate(self, info, user, session, action, timestamp):
        analytics_record = AnalyticsRecord(user_id=user, session=session, action=action, timestamp=timestamp)
        analytics_record.save()
        return CreateAnalyticsRecord(analytics_record=analytics_record)

class Mutation(graphene.ObjectType):
    create_analytics_record = CreateAnalyticsRecord.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)