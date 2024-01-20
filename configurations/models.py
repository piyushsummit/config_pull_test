from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel

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