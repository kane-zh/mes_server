from django_filters.rest_framework import  FilterSet
from apps.production.models.basicinfor_model import *

class ProductionAuditRecordFilters(FilterSet):
    """
    操作记录
    """
    class Meta:
        model = ProductionAuditRecordModel
        fields=["uri"]

class WorkshopInforDefinitionFilters(FilterSet):
    """
    车间信息定义
    """
    class Meta:
        model = WorkshopInforDefinitionModel
        fields=["state","classes","auditor","create_user"]

class TeamInforDefinitionFilters(FilterSet):
    """
    班组信息定义
    """
    class Meta:
        model = TeamInforDefinitionModel
        fields = ["state", "auditor", "create_user", "type"]

class SkillTypeDefinitionFilters(FilterSet):
    """
    技能类型定义
    """
    class Meta:
        model = SkillTypeDefinitionModel
        fields=["state","classes","auditor","create_user"]

class SkillInforDefinitionFilters(FilterSet):
    """
    技能信息定义
    """
    class Meta:
        model = SkillInforDefinitionModel
        fields = ["state", "auditor", "create_user", "type"]

class PersonnelInforDefinitionFilters(FilterSet):
    """
    人员信息定义
    """
    class Meta:
        model = PersonnelInforDefinitionModel
        fields=["create_user","workshop_code","team"]

class AssessmentLevelDefinitionFilters(FilterSet):
    """
    考核等级定义
    """
    class Meta:
        model = AssessmentLevelDefinitionModel
        fields = ["state", "auditor", "create_user"]

class AssessmentTypeDefinitionFilters(FilterSet):
    """
    考核类型定义
    """
    class Meta:
        model = AssessmentTypeDefinitionModel
        fields=["state","classes","auditor","create_user"]

class ProductionBoardFilters(FilterSet):
    """
    生产看板定义
    """
    class Meta:
            model = ProductionBoardModel
            fields = ["state", "auditor", "create_user"]