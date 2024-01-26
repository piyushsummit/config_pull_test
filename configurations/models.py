from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel, TimeFramedModel
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

# Create your models here.
class Configuration(UUIDModel, TimeStampedModel):

    TAB_DETAILS = "tab_details"
    PRE_ASSESSMENT = "pre_assessment"
    BORROWER_UI_COMMON = "borrower_ui_common"
    BORROWER_UI = "borrower_ui"
    BACKOFFICE_UI = "backoffice_ui"
    BACKOFFICE_CONFIG = "backoffice_config"
    KYC = "kyc"
    DOCUMENTATION_SYSTEM = "documentation_system"
    START_TABS = "start_tabs"
    END_TABS = "end_tabs"
    ORGANIZATION_CONFIG = "organization_config"
    PRODUCT_CONFIG = "product_config"
    PRELIMINARY_DOCUMENT = "preliminary_document"
    BORROWER_NOTIFICATION_CONFIG = "borrower_notifications"
    LENDER_NOTIFICATION_CONFIG = "lender_notifications"
    SECURITY_CONFIG = "security"
    ESIGN_CONFIG = "esign_config"
    PRODUCT_VALIDATION = "product_validation"
    BOARDING_DOCUMENT_EXTRACT = "boarding_document_extract"
    RISK_REVIEW_CONFIG = "risk_review_config"
    CONDITIONAL_RISK_REVIEW = "conditional_risk_review"
    LOAN_EXCEPTIONS_CONFIG = "loan_exceptions_config"
    INTEGRATION_CONFIG = "integration_config"
    CBR_AGGREGATION = "cbr_aggregation"
    FEMA = "fema"
    FICO = "fico"
    EXPERIAN = "experian"
    SERVICE_REQUESTS = "service_requests"
    TAX_TRANSCRIPT = "tax"
    ANNUAL_REVIEW = "annual_review"
    QUESTIONAIRE = "questionaire"
    FICO_AGGREGATOR = "fico-aggregator"
    FICO_AGGREGATOR_CONFIG = "fico-aggregator-config"
    FICO_AGGREGATOR_FUNC = "fico-aggregator-func"
    EXPERIAN_AGGREGATOR = "experian-aggregator"
    EXPERIAN_AGGREGATOR_CONFIG = "experian-aggregator-config"
    EXPERIAN_AGGREGATOR_FUNC = "experian-aggregator-func"
    FICO_MAPPER = "fico-mapper"
    EXPERIAN_MAPPER = "experian-mapper"
    CBR_MAPPER_CONFIG = "cbr-mapper-config"
    CBR_MAPPER_FUNC = "cbr-mapper-func"
    IT_SERVICE_NOTIFICATION_CONFIG = "it_notifications"
    SSO = "sso"
    RERUN_CONFIG = "rerun_config"
    PROPERTY_REPORT_SPEC = "property-report-spec"
    SPREAD_TEMPLATE_BUSINESS = "business_spread_template"
    SPREAD_TEMPLATE_GLOBAL = "global_spread_template"
    SPREAD_TEMPLATE_INDIVIDUAL = "individual_spread_template"
    SPREAD_TEMPLATE_CRE_GLOBAL = "cre_global_spread_template"
    SPREAD_TEMPLATE_CRE_OFFICE = "cre_office_spread_template"
    SPREAD_TEMPLATE_CRE_MULTIFAMILY = "cre_multifamily_spread_template"
    SPREAD_TEMPLATE_CRE_OFFICE_ANNUAL = "cre_office_annual_spread_template"
    SPREAD_TEMPLATE_CRE_MULTIFAMILY_ANNUAL = "cre_multifamily_annual_spread_template"
    IT_CONFIG = "it_config"
    ETRAN_TRANSFORMER = "etran_transformer"
    ETRAN_TRANSFORMER_CONFIG = "etran_transformer_config"
    COLLATERAL_DESC_CONFIG = "collateral_desc_config"
    REEVALUATION = "reevaluation"
    EBILLING_PAYMENTS = "ebilling_payments"
    ETRAN = "etran"
    WKFS_TRANSFORMER_CONFIG = "wkfs_transformer_config"
    WKFS_ADMIN_CONFIG_LA = "wkfs_admin_config_LA"
    REASON_TEST_MAPPING = "reason_test_mapping"
    CORELOGIC_TRANSFORMER_SPEC = "corelogic_transformer_spec"
    FINANCIAL_DATA_AGGREGATOR = "financial_data_aggregator"
    FORM5C_SPEC = "form5c_spec"
    FORM5_SPEC = "form5_spec"
    PLESIONYMS_CONFIG = "plesionyms_config"
    CREDIT_BUREAU_TESTS = "credit_bureau_tests"
    DEBT_ACCOUNT_TYPES = "debt_account_types"
    RECONSIDERATION_CONFIG = "reconsideration_config"
    RATE_CONFIG = "rate_config"
    TAXGUARD_NORMALIZER_SPEC = "taxguard_normalizer_spec"
    CI_CSI_CREATE_LOAN_DPH = "ci-etran-create_loan_dph"
    CI_CSI_CREATE_LOAN_DPB = "ci-etran-create_loan_dpb"
    CI_CSI_CREATE_LOAN = "ci-etran-create_loan"
    CI_ETRAN_LOAN_TYPE = "ci-etran-loan-type"
    CI_TENANT_MAP = "ci-tenant-map"
    CI_ETRAN_COMMON = "ci-etran-common"
    CI_ETRAN_DISBURSEMENT = "ci-etran-create_disb"
    CI_ETRAN_SERVICING_DEFERMENT = "ci-etran-servicing_deferment"
    CI_ETRAN_LOANSTATUSCODE = "ci-etran-loanstatuscode"
    CI_ETRAN_DISBURSEMENT_MOBILEHOME = "ci-etran-create_disb_mobilehome"
    CI_ETRAN_UPDATE_LOANAMT_DPB = "ci-etran-update_loanamt_dpb"
    CI_ETRAN_UPDATE_LOANAMT_DPH = "ci-etran-update_loanamt_dph"
    CI_ETRAN_CANCEL_LOAN = "ci-etran-cancel_loan"
    CI_ETRAN_DIFF_ORIGINAL_PAYLOAD_DPB = "ci-etran-diff_original_payload_dpb"
    CI_ETRAN_DIFF_ORIGINAL_PAYLOAD_DPH = "ci-etran-diff_original_payload_dph"
    CI_ETRAN_DIFF_UPDATED_PAYLOAD_DPB = "ci-etran-diff_updated_payload_dpb"
    CI_ETRAN_DIFF_UPDATED_PAYLOAD_DPH = "ci-etran-diff_updated_payload_dph"
    CI_ETRAN_DISB_UOP_THRESHOLD = "ci-etran-disb-uop-threshold"
    CONVERSION = "conversion"
    CI_ETRAN_REINSTATE_LOAN = "ci-etran-reinstate_loan"
    MITIGATION = "mitigation"
    LENDER_MATCH = "lender_match"

    INTERFACE_TYPE_CHOICES = (
        (TAB_DETAILS, "Tab Details"),
        (PRE_ASSESSMENT, "Pre Assessment"),
        (BORROWER_UI_COMMON, "borrower_ui_common"),
        (BORROWER_UI, "Borrower UI"),
        (BACKOFFICE_UI, "Backoffice UI"),
        (BACKOFFICE_CONFIG, "Backoffice Config"),
        (KYC, "KYC"),
        (DOCUMENTATION_SYSTEM, "WKFS"),
        (START_TABS, "Initial Tabs on UI"),
        (END_TABS, "Final Tabs on UI"),
        (ORGANIZATION_CONFIG, "Organization Configuration"),
        (PRODUCT_CONFIG, "Product Configuration"),
        (PRELIMINARY_DOCUMENT, "Preliminary Document"),
        (BORROWER_NOTIFICATION_CONFIG, "Borrower Notification Configuration"),
        (LENDER_NOTIFICATION_CONFIG, "Lender Notification Configuration"),
        (SECURITY_CONFIG, "Security Configuration"),
        (ESIGN_CONFIG, "Esign Configuration"),
        (PRODUCT_VALIDATION, "Product Validation"),
        (BOARDING_DOCUMENT_EXTRACT, "Boarding Document Extract"),
        (RISK_REVIEW_CONFIG, "Risk Review Configuration"),
        (CONDITIONAL_RISK_REVIEW, "Conditional Risk Review"),
        (CBR_AGGREGATION, "CBR Aggregation Configuration"),
        (FICO, "FICO"),
        (EXPERIAN, "EXPERIAN"),
        (SERVICE_REQUESTS, "Service Requests"),
        (TAX_TRANSCRIPT, "Tax Transcript Configuration"),
        (ANNUAL_REVIEW, "Annual Review Configuration"),
        (QUESTIONAIRE, "Questionaire"),
        (FICO_AGGREGATOR, "Fico Aggregation Specifications"),
        (FICO_AGGREGATOR_CONFIG, "Input for Fico Aggregation"),
        (FICO_AGGREGATOR_FUNC, "Functions utilized in Fico Aggregator JQ"),
        (EXPERIAN_AGGREGATOR, "Experian Aggregation Specifications"),
        (EXPERIAN_AGGREGATOR_CONFIG, "Input for Experian Aggregation"),
        (EXPERIAN_AGGREGATOR_FUNC, "Functions utilized in Experian Aggregator JQ"),
        (EXPERIAN_MAPPER, "Experian Codes Mapper Specification"),
        (FICO_MAPPER, "Fico Codes Mapper Specification"),
        (CBR_MAPPER_CONFIG, "Input for CBR Codes Mapper"),
        (CBR_MAPPER_FUNC, "Functions Utilized in CBR Mapper JQ"),
        (IT_SERVICE_NOTIFICATION_CONFIG, "IT Service Request Notification Configuration"),
        (SSO, "SSO Configurations"),
        (LOAN_EXCEPTIONS_CONFIG, "Loan Exceptions Configuration"),
        (RERUN_CONFIG, "Rerun Configuration"),
        (PROPERTY_REPORT_SPEC, "Property Report Spec configuration"),
        (SPREAD_TEMPLATE_BUSINESS, "Spreading Template - Business"),
        (SPREAD_TEMPLATE_GLOBAL, "Spreading Template - Global"),
        (SPREAD_TEMPLATE_INDIVIDUAL, "Spreading Template - Individual"),
        (SPREAD_TEMPLATE_CRE_OFFICE, "Spreading Template - CRE Office"),
        (SPREAD_TEMPLATE_CRE_GLOBAL, "Spreading Template - CRE Global"),
        (SPREAD_TEMPLATE_CRE_MULTIFAMILY, "Spreading Template - CRE Multifamily"),
        (SPREAD_TEMPLATE_CRE_OFFICE_ANNUAL, "Spreading Template - CRE Office - Annual"),
        (SPREAD_TEMPLATE_CRE_MULTIFAMILY_ANNUAL, "Spreading Template - CRE Multifamily - Annual"),
        (IT_CONFIG, "IT Service Request configuration"),
        (ETRAN_TRANSFORMER, "Etran Transformer Specifications"),
        (ETRAN_TRANSFORMER_CONFIG, "Input for Etran Transformer"),
        (COLLATERAL_DESC_CONFIG, "Description text for all collateral types"),
        (SSO, "SSO Configurations"),
        (REEVALUATION, "Re-evaluation"),
        (EBILLING_PAYMENTS, "E-billing Payments"),
        (ETRAN, "E-tran configuration"),
        (WKFS_TRANSFORMER_CONFIG, "WKFS Transformer Config"),
        (WKFS_ADMIN_CONFIG_LA, "WKFS Admin Config LA"),
        (REASON_TEST_MAPPING, "Reason Test Mapping"),
        (CORELOGIC_TRANSFORMER_SPEC, "Corelogic Transformer Spec"),
        (FINANCIAL_DATA_AGGREGATOR, "financial_data_aggregator"),
        (FORM5C_SPEC, "Form 5C Spec"),
        (FORM5_SPEC, "FORM 5 Spec"),
        (PLESIONYMS_CONFIG, "Plesionyms Config"),
        (CREDIT_BUREAU_TESTS, "Credit Bureau Exception Tests"),
        (DEBT_ACCOUNT_TYPES, "Debt Account Types"),
        (RECONSIDERATION_CONFIG, "Reconsideration Config"),
        (TAXGUARD_NORMALIZER_SPEC, "Taxguard Normalizer Spec"),
        (CI_CSI_CREATE_LOAN_DPH, "ci-etran-create_loan_dph"),
        (CI_CSI_CREATE_LOAN_DPB, "ci-etran-create_loan_dpb"),
        (CI_CSI_CREATE_LOAN, "ci-etran-create_loan"),
        (RATE_CONFIG, "Rate Config"),
        (CI_TENANT_MAP, "ci-tenant-map"),
        (CI_ETRAN_LOAN_TYPE, "ci-etran-loan-type"),
        (FEMA, "FEMA"),
        (CI_ETRAN_COMMON, "ci-etran-common"),
        (CI_ETRAN_DISBURSEMENT, "ci-etran-create_disb"),
        (INTEGRATION_CONFIG, "Integration Configuration"),
        (CI_ETRAN_SERVICING_DEFERMENT, "ci-etran-servicing_deferment"),
        (CI_ETRAN_LOANSTATUSCODE, "ci-etran-loanstatuscode"),
        (CI_ETRAN_DISBURSEMENT_MOBILEHOME, "ci-etran-create_disb_mobilehome"),
        (CI_ETRAN_UPDATE_LOANAMT_DPB, "ci-etran-update_loanamt_dpb"),
        (CI_ETRAN_UPDATE_LOANAMT_DPH, "ci-etran-update_loanamt_dph"),
        (CI_ETRAN_CANCEL_LOAN, "ci-etran-cancel_loan"),
        (CI_ETRAN_DIFF_ORIGINAL_PAYLOAD_DPB, "ci-etran-diff_original_payload_dpb"),
        (CI_ETRAN_DIFF_ORIGINAL_PAYLOAD_DPH, "ci-etran-diff_original_payload_dph"),
        (CI_ETRAN_DIFF_UPDATED_PAYLOAD_DPH, "ci-etran-diff_updated_payload_dph"),
        (CI_ETRAN_DIFF_UPDATED_PAYLOAD_DPB, "ci-etran-diff_updated_payload_dpb"),
        (CI_ETRAN_DISB_UOP_THRESHOLD, "ci-etran-disb-uop-threshold"),
        (CONVERSION, "DCMS conversion"),
        (CI_ETRAN_REINSTATE_LOAN, "ci-etran-reinstate_loan"),
        (MITIGATION, "Mitigation Suggestions"),
        (LENDER_MATCH, "Lender Match Settings"),
    )

    interface_type = models.CharField("Interface Type", max_length=255, choices=INTERFACE_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    details = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return f"{self.name}, {self.interface_type}"
    

class DisasterDeclaration(UUIDModel, TimeStampedModel):

    EIDL = "0"
    DEPT_OF_AG_EIDL = "1"
    EARTHQUAKES = "2"
    EXPLOSIONS = "4"
    FIRES = "5"
    FLOODS = "6"
    FREEZES = "7"
    HURRICANES = "8"
    LANDSLIDES_MUDSLIDES = "9"
    STORMS = "B"
    TORNADOES = "C"
    VOLCANIC_ERUPTIONS = "D"
    OTHER_NATURAL = "E"
    OTHER_MANMADE = "F"
    UNKNOWN = "U"

    DAMAGE_TYPE_CHOICES = (
        (EIDL, f"{EIDL} - EIDL"),
        (DEPT_OF_AG_EIDL, f"{DEPT_OF_AG_EIDL} - DEPT OF AG(FSA) EIDL"),
        (EARTHQUAKES, f"{EARTHQUAKES} - EARTHQUAKES"),
        (EXPLOSIONS, f"{EXPLOSIONS} - EXPLOSIONS"),
        (FIRES, f"{FIRES} - FIRES"),
        (FLOODS, f"{FLOODS} - FLOODS"),
        (FREEZES, f"{FREEZES} - FREEZES"),
        (HURRICANES, f"{HURRICANES} - HURRICANES"),
        (LANDSLIDES_MUDSLIDES, f"{LANDSLIDES_MUDSLIDES} - LANDSLIDES/MUDSLIDES"),
        (STORMS, f"{STORMS} - STORMS"),
        (TORNADOES, f"{TORNADOES} - TORNADOES"),
        (VOLCANIC_ERUPTIONS, f"{VOLCANIC_ERUPTIONS} - VOLCANIC ERUPTIONS"),
        (OTHER_NATURAL, f"{OTHER_NATURAL} - OTHER: NATURAL"),
        (OTHER_MANMADE, f"{OTHER_MANMADE} - OTHER: MANMADE"),
        (UNKNOWN, f"{UNKNOWN} - UNKNOWN"),
    )

    # FIXME - remove these once we know they've been replaced everywhere
    SBA_DECLARATION = 0
    GOVERNOR_CERT = 1
    MILITARY_RESERVIST_EIDL = 2
    PRESIDENTIAL_IA = 3
    PRESIDENTIAL_PA = 4
    AG_SECRETARY = 5

    DISASTER_NEW = 0
    PREPARING_SURVEY = 1
    SURVEY_IN_PROGRESS = 2
    PENDING_SURVEY_VALIDATION = 3
    SURVEY_VALIDATED = 4
    FEMA_DECLINED = 5
    FOC_REVIEW = 6
    RESURVEY_REQUESTED = 7
    ODA_REVIEW = 8
    ODA_APPROVED = 9
    PENDING_ADMIN_APPROVAL = 10
    DISASTER_DECLARED = 11
    AMEND_REQUESTED = 12
    DISASTER_CANCELED = 13

    DECLARATION_STATUS_CHOICES = (
        (DISASTER_NEW, "Disaster New"),
        (PREPARING_SURVEY, "Preparing Survey"),
        (SURVEY_IN_PROGRESS, "Survey In Progress"),
        (PENDING_SURVEY_VALIDATION, "Pending Survey Validation"),
        (SURVEY_VALIDATED, "Survey Validated"),
        (FEMA_DECLINED, "FEMA Declined"),
        (FOC_REVIEW, "Survey Review"),
        (RESURVEY_REQUESTED, "Resurvey Requested"),
        (ODA_REVIEW, "Declaration Review"),
        (ODA_APPROVED, "Declaration Approved"),
        (PENDING_ADMIN_APPROVAL, "Pending Admin Approval"),
        (DISASTER_DECLARED, "Disaster Declared"),
        (AMEND_REQUESTED, "Amend Requested"),
        (DISASTER_CANCELED, "Disaster Canceled"),
    )

    STATE_WITHDRAW = "state_withdraw"
    SBA_DECLINE = "sba_decline"
    VOID = "void"

    CANCEL_CHOICES = (
        (STATE_WITHDRAW, "State Withdraw"),
        (SBA_DECLINE, "SBA Decline"),
        (VOID, "Void"),
    )

    EIDL_PURPOSE = "eidl"
    PHYSICAL = "physical"
    MREIDL = "mreidl"

    PURPOSE_CHOICES = (
        (EIDL_PURPOSE, "EIDL"),
        (MREIDL, "MREIDL"),
        (PHYSICAL, "Physical Damage"),
    )

    db_disaster_number = models.PositiveIntegerField(null=True, blank=True)
    disaster_number = models.CharField(_("Disaster Number"), max_length=255, blank=True, default="")
    db_physical_damage_number = models.PositiveIntegerField(null=True, blank=True)
    db_eidl_damage_number = models.PositiveIntegerField(null=True, blank=True)
    disaster_description = models.CharField(_("Disaster Description"), max_length=255, blank=True, default="")

    disaster_initiator = models.CharField(max_length=128, default="", blank=True, verbose_name=_("Disaster Initiator"))
    primary_disaster_state = models.CharField(_("Primary State"), null=True, blank=True, max_length=100)
    primary_counties = models.JSONField("Primary Locales", blank=True, default=list)
    contiguous_counties = models.JSONField("Contiguous Locales", blank=True, default=list)
    tribal_regions = models.JSONField("Tribal Regions", blank=True, default=list)
    damage_type_code = models.CharField(
        _("Disaster Damage Type"), choices=DAMAGE_TYPE_CHOICES, max_length=2, blank=True, default=""
    )
    contact_person = models.CharField(_("Contact Person"), max_length=255, blank=True, default="")
    form_605_remarks = models.TextField(_("Form 605 Remarks"), blank=True, default="")

    disaster_status = models.IntegerField(
        _("Disaster Status"), choices=DECLARATION_STATUS_CHOICES, null=True, blank=True, default=0
    )
    fema_number = models.CharField(_("FEMA Number"), max_length=255, blank=True, default="")
    usda_agency_number = models.CharField(_("USDA Agency Number"), max_length=255, blank=True, default="")
    incident_start_date = models.DateField(_("Incident Start Date"), null=True, blank=True)
    incident_end_date = models.DateField(_("Incident End Date"), null=True, blank=True)
    request_date = models.DateField(_("Request Date"), null=True, blank=True)
    received_date = models.DateField(_("Received Date"), null=True, blank=True)
    geographic_multiplier = models.DecimalField(
        _("Geographic Multiplier"), max_digits=6, decimal_places=3, null=True, blank=True
    )
    physical_declaration_number = models.CharField(
        _("Physical Declaration Number"), max_length=255, blank=True, default=""
    )
    physical_deadline_date = models.DateField(_("Physical Deadline Date"), null=True, blank=True)
    physical_unsecured_limit = models.DecimalField(
        _("Physical Unsecured Limit"), max_digits=16, decimal_places=2, null=True, blank=True, default=25000
    )
    eidl_declaration_number = models.CharField(_("EIDL Declaration Number"), max_length=255, blank=True, default="")
    eidl_deadline_date = models.DateField(_("EIDL Deadline Date"), null=True, blank=True)
    eidl_unsecured_limit = models.DecimalField(
        _("EIDL Unsecured Limit"), max_digits=16, decimal_places=2, null=True, blank=True, default=25000
    )
    declaration_date = models.DateField(_("Declaration Date"), null=True, blank=True)
    disbursement_period_months = models.IntegerField(_("Disbursement Period (Months)"), default=6)
    grace_period_days = models.IntegerField(_("Grace Period (Days)"), default=15)
    payment_deferment_period_months = models.IntegerField(_("Payment Deferment Period"), default=11)
    first_payment_due_months = models.IntegerField(_("First Payment Due"), default=12)
    initial_disbursement_limit = models.IntegerField(
        _("Amount that can be initially disbursed for a loan"), default=50000
    )
    is_active = models.BooleanField(_("Is Active"), default=True)

    naics_code_set = models.IntegerField(blank=True, null=True, verbose_name=_("NAICS Data Set Year"))

    interest_rate = models.JSONField("Interest Rate", blank=True, default=dict)
    is_survey_required = models.BooleanField(_("Is Survey Required"), default=True)

    is_ulp_serviced = models.BooleanField(_("Is ULP Serviced"), default=False)

    cancel_notes = models.TextField(blank=True, null=True)
    cancel_at = models.DateTimeField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=20, choices=CANCEL_CHOICES, null=True, blank=True)
    document_data = models.JSONField("Document Data", blank=True, default=dict)

    source_external_files = models.JSONField(
        "External Files from Legacy system", blank=True, default=list)

    survey_request_date = models.DateField(_("Survey Request Date"), null=True, blank=True)
    survey_received_date = models.DateField(_("Survey Received Date"), null=True, blank=True)
    reinstatement_period = models.IntegerField(_("Reinstatement Period (Days)"), default=60)
    signer_details = models.JSONField(blank=True, default=dict)

class ProductType(UUIDModel, TimeStampedModel):
    class Meta:
        permissions = [
            ("can_view_product_types", "Can View Product Types"),
        ]

    LOC = "LOC"
    TL = "TL"
    SR = "SR"
    EL = "EL"
    DL = "DL"

    PRODUCT_TYPE_CODE_CHOICES = (
        (LOC, "Line of Credit"),
        (TL, "Term Loan"),
        (SR, "Service Request"),
        (EL, "SBA Express Loan"),
        (DL, "Disaster Business Loan"),
    )

    name = models.CharField("Product Type Name", max_length=250, unique=True)
    description = models.TextField("Product Type Description", blank=True, null=True)
    product_type_code = models.CharField(
        "Product Type Code",
        choices=PRODUCT_TYPE_CODE_CHOICES,
        max_length=15,
        unique=True,
    )

    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Product(UUIDModel, TimeFramedModel, TimeStampedModel):
    PRODUCT_CODE_HOME = "DLAP5C"
    PRODUCT_CODE_BUSINESS = "DLAP5"

    class Meta:
        permissions = [
            ("can_view_products", "Can View Products"),
        ]

    STATUS = Choices(("draft", "Draft"), ("active", "Active"), ("inactive", "Inactive"))

    name = models.CharField("Product Name", max_length=250, unique=True)
    description = models.TextField("Product Description", blank=True, null=True)
    product_code = models.CharField(
        "Product Code",
        max_length=15,
        blank=True,
        null=True,
        unique=True,
    )
    fi_product_code = models.CharField("FI Product Code", max_length=255, null=True, blank=True, unique=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)

    min_term_in_months = models.PositiveSmallIntegerField("Min Term in Months", default=1)
    max_term_in_months = models.PositiveSmallIntegerField("Max Term in Months", default=180)
    min_rate = models.FloatField("Minimum Interest Rate", default=0.0)
    max_rate = models.FloatField("Maximum Interest Rate", default=36.0)
    is_express_loan = models.BooleanField(default=False)
    is_demand_feature_loan = models.BooleanField(default=False)
    is_multiterm = models.BooleanField(default=False)
    file_due_in_days = models.PositiveSmallIntegerField(default=14)

    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.name)

class Loan(UUIDModel, TimeStampedModel):
    status = models.CharField(max_length=10, default="Pending")
    details = models.JSONField(blank=True, default=dict)

class FlutterLoan(UUIDModel, TimeStampedModel):
    status = models.CharField(max_length=10, default="Pending")
    details = models.JSONField(blank=True, default=dict)