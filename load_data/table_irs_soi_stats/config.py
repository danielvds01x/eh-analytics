# Define the field mapping dictionary with readable names and original                                                              descriptions
FIELD_MAPPING =   {
    'STATEFIPS':  {'data_type': 'String', 'readable_name': 'state_fips_code', '                                                     description': 'The State Federal Information Processing System (FIPS) code'},
    'STATE':      {'data_type': 'String', 'readable_name': 'state', '                                                               description': 'The State associated with the ZIP code'},
    'ZIPCODE':    {'data_type': 'String', 'readable_name': 'zip_code', '                                                            description': '5_digit Zip code'},
    'AGI_STUB':   {'data_type': 'Int'   , 'readable_name': 'size_of_adjusted_gross_income', '                                       description': 'Size of adjusted gross income'},
    'N1':         {'data_type': 'Double', 'readable_name': 'num_returns', '                                                         description': 'Number of returns'},
    'MARS1':      {'data_type': 'Double', 'readable_name': 'num_single_returns', '                                                  description': 'Number of single returns'},
    'MARS2':      {'data_type': 'Double', 'readable_name': 'num_joint_returns', '                                                   description': 'Number of joint returns'},
    'MARS4':      {'data_type': 'Double', 'readable_name': 'num_head_of_household_returns', '                                       description': 'Number of head of household returns'},
    'ELF':        {'data_type': 'Double', 'readable_name': 'num_electronically_filed_returns', '                                    description': 'Number of electronically filed returns'},
    'CPREP':      {'data_type': 'Double', 'readable_name': 'num_computer_prepared_paper_returns', '                                 description': 'Number of computer prepared paper returns'},
    'PREP':       {'data_type': 'Double', 'readable_name': 'num_returns_with_paid_preparers_signature', '                           description': "Number of returns with paid preparer's signature"},
    'DIR_DEP':    {'data_type': 'Double', 'readable_name': 'num_returns_with_direct_deposit', '                                     description': 'Number of returns with direct deposit'},
    'VRTCRIND':   {'data_type': 'Double', 'readable_name': 'num_returns_with_virtual_currency_indicator', '                         description': 'Number of returns with virtual currency indicator'},
    'N2':         {'data_type': 'Double', 'readable_name': 'num_individuals', '                                                     description': 'Number of individuals'},
    'TOTAL_VITA': {'data_type': 'Double', 'readable_name': 'total_num_volunteer_prepared_returns', '                                description': 'Total number of volunteer prepared returns'},
    'VITA':       {'data_type': 'Double', 'readable_name': 'num_vita_prepared_returns', '                                           description': 'Number of volunteer income tax assistance (VITA) prepared returns'},
    'TCE':        {'data_type': 'Double', 'readable_name': 'num_tce_prepared_returns', '                                            description': 'Number of tax counseling for the elderly (TCE) prepared returns'},
    'VITA_EIC':   {'data_type': 'Double', 'readable_name': 'num_volunteer_prepared_returns_with_earned_income_credit', '            description': 'Number of volunteer prepared returns with Earned Income Credit'},
    'RAC':        {'data_type': 'Double', 'readable_name': 'num_refund_anticipation_check_returns', '                               description': 'Number of refund anticipation check returns'},
    'ELDERLY':    {'data_type': 'Double', 'readable_name': 'num_elderly_returns', '                                                 description': 'Number of elderly returns'},
    'A00100':     {'data_type': 'Double', 'readable_name': 'adjusted_gross_income', '                                               description': 'Adjust gross income (AGI)'},
    'N02650':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_income', '                                       description': 'Number of returns with total income'},
    'A02650':     {'data_type': 'Double', 'readable_name': 'total_income_amount', '                                                 description': 'Total income amount'},
    'N00200':     {'data_type': 'Double', 'readable_name': 'num_returns_with_salaries_wages', '                                     description': 'Number of returns with salaries and wages'},
    'A00200':     {'data_type': 'Double', 'readable_name': 'salaries_wages_amount', '                                               description': 'Salaries and wages amount'},
    'N00300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_taxable_interest', '                                   description': 'Number of returns with taxable interest'},
    'A00300':     {'data_type': 'Double', 'readable_name': 'taxable_interest_amount', '                                             description': 'Taxable interest amount'},
    'N00600':     {'data_type': 'Double', 'readable_name': 'num_returns_with_ordinary_dividends', '                                 description': 'Number of returns with ordinary dividends'},
    'A00600':     {'data_type': 'Double', 'readable_name': 'ordinary_dividends_amount', '                                           description': 'Ordinary dividends amount'},
    'N00650':     {'data_type': 'Double', 'readable_name': 'num_returns_with_qualified_dividends', '                                description': 'Number of returns with qualified dividends'},
    'A00650':     {'data_type': 'Double', 'readable_name': 'qualified_dividends_amount', '                                          description': 'Qualified dividends amount'},
    'N00700':     {'data_type': 'Double', 'readable_name': 'num_returns_with_state_local_income_tax_refunds', '                     description': 'Number of returns with state and local income tax refunds'},
    'A00700':     {'data_type': 'Double', 'readable_name': 'state_local_income_tax_refunds_amount', '                               description': 'State and local income tax refunds amount'},
    'N00900':     {'data_type': 'Double', 'readable_name': 'num_returns_with_business_professional_net_income', '                   description': 'Number of returns with business or professional net income (less loss)'},
    'A00900':     {'data_type': 'Double', 'readable_name': 'business_professional_net_income_amount', '                             description': 'Business or professional net income (less loss) amount'},
    'N01000':     {'data_type': 'Double', 'readable_name': 'num_returns_with_net_capital_gain', '                                   description': 'Number of returns with net capital gain (less loss)'},
    'A01000':     {'data_type': 'Double', 'readable_name': 'net_capital_gain_amount', '                                             description': 'Net capital gain (less loss) amount'},
    'N01400':     {'data_type': 'Double', 'readable_name': 'num_returns_with_taxable_ira_distributions', '                          description': 'Number of returns with taxable individual retirement arrangements distributions'},
    'A01400':     {'data_type': 'Double', 'readable_name': 'taxable_ira_distributions_amount', '                                    description': 'Taxable individual retirement arrangements distributions amount'},
    'N01700':     {'data_type': 'Double', 'readable_name': 'num_returns_with_taxable_pensions_annuities', '                         description': 'Number of returns with taxable pensions and annuities'},
    'A01700':     {'data_type': 'Double', 'readable_name': 'taxable_pensions_annuities_amount', '                                   description': 'Taxable pensions and annuities amount'},
    'SCHF':       {'data_type': 'Double', 'readable_name': 'num_farm_returns', '                                                    description': 'Number of farm returns'},
    'N02300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_unemployment_compensation', '                          description': 'Number of returns with unemployment compensation'},
    'A02300':     {'data_type': 'Double', 'readable_name': 'unemployment_compensation_amount', '                                    description': 'Unemployment compensation amount'},
    'N02500':     {'data_type': 'Double', 'readable_name': 'num_returns_with_taxable_social_security_benefits', '                   description': 'Number of returns with taxable Social Security benefits'},
    'A02500':     {'data_type': 'Double', 'readable_name': 'taxable_social_security_benefits_amount', '                             description': 'Taxable Social Security benefits amount'},
    'N26270':     {'data_type': 'Double', 'readable_name': 'num_returns_with_partnership_s_corp_net_income', '                      description': 'Number of returns with partnership/S_corp net income (less loss)'},
    'A26270':     {'data_type': 'Double', 'readable_name': 'partnership_s_corp_net_income_amount', '                                description': 'Partnership/S_corp net income (less loss) amount'},
    'N02900':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_statutory_adjustments', '                        description': 'Number of returns with total statutory adjustments'},
    'A02900':     {'data_type': 'Double', 'readable_name': 'total_statutory_adjustments_amount', '                                  description': 'Total statutory adjustments amount'},
    'N03220':     {'data_type': 'Double', 'readable_name': 'num_returns_with_educator_expenses', '                                  description': 'Number of returns with educator expenses'},
    'A03220':     {'data_type': 'Double', 'readable_name': 'educator_expenses_amount', '                                            description': 'Educator expenses amount'},
    'N03300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_self_employed_keogh_retirement_plans', '               description': 'Number of returns with Self_employed (Keogh) retirement plans'},
    'A03300':     {'data_type': 'Double', 'readable_name': 'self_employed_keogh_retirement_plans_amount', '                         description': 'Self_employed (Keogh) retirement plans amount'},
    'N03270':     {'data_type': 'Double', 'readable_name': 'num_returns_with_self_employed_health_insurance_deduction', '           description': 'Number of returns with Self_employed health insurance deduction'},
    'A03270':     {'data_type': 'Double', 'readable_name': 'self_employed_health_insurance_deduction_amount', '                     description': 'Self_employed health insurance deduction amount'},
    'N03150':     {'data_type': 'Double', 'readable_name': 'num_returns_with_individual_retirement_arrangement_payments', '         description': 'Number of returns with Individual retirement arrangement payments'},
    'A03150':     {'data_type': 'Double', 'readable_name': 'individual_retirement_arrangement_payments_amount', '                   description': 'Individual retirement arrangement payments amount'},
    'N03210':     {'data_type': 'Double', 'readable_name': 'num_returns_with_student_loan_interest_deduction', '                    description': 'Number of returns with student loan interest deduction'},
    'A03210':     {'data_type': 'Double', 'readable_name': 'student_loan_interest_deduction_amount', '                              description': 'Student loan interest deduction amount'},
    'N02910':     {'data_type': 'Double', 'readable_name': 'num_returns_with_charitable_contributions_if_took_standard_deduction', 'description': 'Number of returns with charitable contributions if took standard deduction'},
    'A02910':     {'data_type': 'Double', 'readable_name': 'charitable_contributions_if_took_standard_deduction', '                 description': 'Charitable contributions if took standard deduction'},
    'N04450':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_standard_deduction', '                           description': 'Number of returns with total standard deduction'},
    'A04450':     {'data_type': 'Double', 'readable_name': 'total_standard_deduction_amount', '                                     description': 'Total standard deduction amount'},
    'N04100':     {'data_type': 'Double', 'readable_name': 'num_returns_with_basic_standard_deduction', '                           description': 'Number of returns with basic standard deduction'},
    'A04100':     {'data_type': 'Double', 'readable_name': 'basic_standard_deduction_amount', '                                     description': 'Basic standard deduction amount'},
    'N04200':     {'data_type': 'Double', 'readable_name': 'num_returns_with_additional_standard_deduction', '                      description': 'Number of returns with additional standard deduction'},
    'A04200':     {'data_type': 'Double', 'readable_name': 'additional_standard_deduction_amount', '                                description': 'Additional standard deduction amount'},
    'N04470':     {'data_type': 'Double', 'readable_name': 'num_returns_with_itemized_deductions', '                                description': 'Number of returns with itemized deductions'},
    'A04470':     {'data_type': 'Double', 'readable_name': 'total_itemized_deductions_amount', '                                    description': 'Total itemized deductions amount'},
    'A00101':     {'data_type': 'Double', 'readable_name': 'agi_for_itemized_returns_amount', '                                     description': 'Amount of AGI for itemized returns'},
    'N17000':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_medical_and_dental_expense_deduction', '         description': 'Number of returns with Total medical and dental expense deduction'},
    'A17000':     {'data_type': 'Double', 'readable_name': 'total_medical_and_dental_expense_deduction_amount', '                   description': 'Total medical and dental expense deduction amount'},
    'N18425':     {'data_type': 'Double', 'readable_name': 'num_returns_with_state_and_local_income_taxes', '                       description': 'Number of returns with State and local income taxes'},
    'A18425':     {'data_type': 'Double', 'readable_name': 'state_and_local_income_taxes_amount', '                                 description': 'State and local income taxes amount'},
    'N18450':     {'data_type': 'Double', 'readable_name': 'num_returns_with_state_and_local_general_sales_tax', '                  description': 'Number of returns with State and local general sales tax'},
    'A18450':     {'data_type': 'Double', 'readable_name': 'state_and_local_general_sales_tax_amount', '                            description': 'State and local general sales tax amount'},
    'N18500':     {'data_type': 'Double', 'readable_name': 'num_returns_with_real_estate_taxes', '                                  description': 'Number of returns with real estate taxes'},
    'A18500':     {'data_type': 'Double', 'readable_name': 'real_estate_taxes_amount', '                                            description': 'Real estate taxes amount'},
    'N18800':     {'data_type': 'Double', 'readable_name': 'num_returns_with_personal_property_taxes', '                            description': 'Number of returns with Personal property taxes'},
    'A18800':     {'data_type': 'Double', 'readable_name': 'personal_property_taxes_amount', '                                      description': 'Personal property taxes amount'},
    'N18460':     {'data_type': 'Double', 'readable_name': 'num_returns_with_limited_state_and_local_taxes', '                      description': 'Number of returns with Limited state and local taxes'},
    'A18460':     {'data_type': 'Double', 'readable_name': 'limited_state_and_local_taxes_amount', '                                description': 'Limited state and local taxes'},
    'N18300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_taxes_paid', '                                   description': 'Number of returns with Total taxes paid'},
    'A18300':     {'data_type': 'Double', 'readable_name': 'total_taxes_paid_amount', '                                             description': 'Total taxes paid amount'},
    'N19300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_home_mortgage_interest_paid', '                        description': 'Number of returns with Home mortgage interest paid'},
    'A19300':     {'data_type': 'Double', 'readable_name': 'home_mortgage_interest_paid_amount', '                                  description': 'Home mortgage interest paid amount'},
    'N19500':     {'data_type': 'Double', 'readable_name': 'num_returns_with_home_mortgage_from_personal_seller', '                 description': 'Number of returns with Home mortgage from personal seller'},
    'A19500':     {'data_type': 'Double', 'readable_name': 'home_mortgage_from_personal_seller_amount', '                           description': 'Home mortgage from personal seller amount'},
    'N19530':     {'data_type': 'Double', 'readable_name': 'num_returns_with_deductible_points', '                                  description': 'Number of returns with Deductible points'},
    'A19530':     {'data_type': 'Double', 'readable_name': 'deductible_points_amount', '                                            description': 'Deductible points amount'},
    'N19550':     {'data_type': 'Double', 'readable_name': 'num_returns_with_qualified_mortgage_insurance_premiums', '              description': 'Number of returns with Qualified mortgage insurance premiums'},
    'A19550':     {'data_type': 'Double', 'readable_name': 'qualified_mortgage_insurance_premiums_amount', '                        description': 'Qualified mortgage insurance premiums amount'},
    'N19570':     {'data_type': 'Double', 'readable_name': 'num_returns_with_investment_interest_paid', '                           description': 'Number of returns with Investment interest paid'},
    'A19570':     {'data_type': 'Double', 'readable_name': 'investment_interest_paid_amount', '                                     description': 'Investment interest paid amount'},
    'N19700':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_charitable_contributions', '                     description': 'Number of returns with Total charitable contributions'},
    'A19700':     {'data_type': 'Double', 'readable_name': 'total_charitable_contributions_amount', '                               description': 'Total charitable contributions amount'},
    'N20950':     {'data_type': 'Double', 'readable_name': 'num_returns_with_other_non_limited_miscellaneous_deductions', '         description': 'Number of returns with Other non_limited miscellaneous deductions'},
    'A20950':     {'data_type': 'Double', 'readable_name': 'other_non_limited_miscellaneous_deductions_amount', '                   description': 'Other non_limited miscellaneous deductions amount'},
    'N04475':     {'data_type': 'Double', 'readable_name': 'num_returns_with_qualified_business_income_deduction', '                description': 'Number of returns with Qualified business income deduction'},
    'A04475':     {'data_type': 'Double', 'readable_name': 'qualified_business_income_deduction_amount', '                          description': 'Qualified business income deduction'},
    'N04800':     {'data_type': 'Double', 'readable_name': 'num_returns_with_taxable_income', '                                     description': 'Number of returns with taxable income'},
    'A04800':     {'data_type': 'Double', 'readable_name': 'taxable_income_amount', '                                               description': 'Taxable income amount'},
    'N05800':     {'data_type': 'Double', 'readable_name': 'num_returns_with_income_tax_before_credits', '                          description': 'Number of returns with income tax before credits'},
    'A05800':     {'data_type': 'Double', 'readable_name': 'income_tax_before_credits_amount', '                                    description': 'Income tax before credits amount'},
    'N09600':     {'data_type': 'Double', 'readable_name': 'num_returns_with_alternative_minimum_tax', '                            description': 'Number of returns with alternative minimum tax'},
    'A09600':     {'data_type': 'Double', 'readable_name': 'alternative_minimum_tax_amount', '                                      description': 'Alternative minimum tax amount'},
    'N05780':     {'data_type': 'Double', 'readable_name': 'num_returns_with_excess_advance_premium_tax_credit_repayment', '        description': 'Number of returns with excess advance premium tax credit repayment'},
    'A05780':     {'data_type': 'Double', 'readable_name': 'excess_advance_premium_tax_credit_repayment_amount', '                  description': 'Excess advance premium tax credit repayment amount'},
    'N07100':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_tax_credits', '                                  description': 'Number of returns with total tax credits'},
    'A07100':     {'data_type': 'Double', 'readable_name': 'total_tax_credits_amount', '                                            description': 'Total tax credits amount'},
    'N07300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_foreign_tax_credit', '                                 description': 'Number of returns with foreign tax credit'},
    'A07300':     {'data_type': 'Double', 'readable_name': 'foreign_tax_credit_amount', '                                           description': 'Foreign tax credit amount'},
    'N07180':     {'data_type': 'Double', 'readable_name': 'num_returns_with_child_and_dependent_care_credit', '                    description': 'Number of returns with child and dependent care credit'},
    'A07180':     {'data_type': 'Double', 'readable_name': 'child_and_dependent_care_credit_amount', '                              description': 'Child and dependent care credit amount'},
    'N07230':     {'data_type': 'Double', 'readable_name': 'num_returns_with_nonrefundable_education_credit', '                     description': 'Number of returns with nonrefundable education credit'},
    'A07230':     {'data_type': 'Double', 'readable_name': 'nonrefundable_education_credit_amount', '                               description': 'Nonrefundable education credit amount'},
    'N07240':     {'data_type': 'Double', 'readable_name': 'num_returns_with_retirement_savings_contribution_credit', '             description': 'Number of returns with retirement savings contribution credit'},
    'A07240':     {'data_type': 'Double', 'readable_name': 'retirement_savings_contribution_credit_amount', '                       description': 'Retirement savings contribution credit amount'},
    'N07225':     {'data_type': 'Double', 'readable_name': 'num_returns_with_child_and_other_dependent_credit', '                   description': 'Number of returns with child and other dependent credit'},
    'A07225':     {'data_type': 'Double', 'readable_name': 'child_and_other_dependent_credit_amount', '                             description': 'Child and other dependent credit amount'},
    'N07260':     {'data_type': 'Double', 'readable_name': 'num_returns_with_residential_energy_tax_credit', '                      description': 'Number of returns with residential energy tax credit'},
    'A07260':     {'data_type': 'Double', 'readable_name': 'residential_energy_tax_credit_amount', '                                description': 'Residential energy tax credit amount'},
    'N09400':     {'data_type': 'Double', 'readable_name': 'num_returns_with_self_employment_tax' , '                               description': 'Number of returns with self_employment tax'},
    'A09400':     {'data_type': 'Double', 'readable_name': 'self_employment_tax_amount', '                                          description': 'Self_employment tax amount'},
    'N85770':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_premium_tax_credit', '                           description': 'Number of returns with total premium tax credit'},
    'A85770':     {'data_type': 'Double', 'readable_name': 'total_premium_tax_credit_amount', '                                     description': 'Total premium tax credit amount'},
    'N85775':     {'data_type': 'Double', 'readable_name': 'num_returns_with_advance_premium_tax_credit', '                         description': 'Number of returns with advance premium tax credit'},
    'A85775':     {'data_type': 'Double', 'readable_name': 'advance_premium_tax_credit_amount', '                                   description': 'Advance premium tax credit amount'},
    'N10600':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_tax_payments', '                                 description': 'Number of returns with total tax payments'},
    'A10600':     {'data_type': 'Double', 'readable_name': 'total_tax_payments_amount', '                                           description': 'Total tax payments amount'},
    'N59660':     {'data_type': 'Double', 'readable_name': 'num_returns_with_earned_income_credit', '                               description': 'Number of returns with earned income credit'},
    'A59660':     {'data_type': 'Double', 'readable_name': 'earned_income_credit_amount', '                                         description': 'Earned income credit amount'},
    'N59720':     {'data_type': 'Double', 'readable_name': 'num_returns_with_excess_earned_income_credit', '                        description': 'Number of returns with excess earned income credit (refundable)'},
    'A59720':     {'data_type': 'Double', 'readable_name': 'excess_earned_income_credit_amount', '                                  description': 'Excess earned income credit (refundable) amount'},
    'N11070':     {'data_type': 'Double', 'readable_name': 'num_returns_with_additional_child_tax_credit', '                        description': 'Number of returns with additional child tax credit'},
    'A11070':     {'data_type': 'Double', 'readable_name': 'additional_child_tax_credit_amount', '                                  description': 'Additional child tax credit amount'},
    'N10960':     {'data_type': 'Double', 'readable_name': 'num_returns_with_refundable_education_credit', '                        description': 'Number of returns with refundable education credit'},
    'A10960':     {'data_type': 'Double', 'readable_name': 'refundable_education_credit_amount', '                                  description': 'Refundable education credit amount'},
    'N11560':     {'data_type': 'Double', 'readable_name': 'num_returns_with_net_premium_tax_credit', '                             description': 'Number of returns with net premium tax credit'},
    'A11560':     {'data_type': 'Double', 'readable_name': 'net_premium_tax_credit_amount', '                                       description': 'Net premium tax credit amount'},
    'N11450':     {'data_type': 'Double', 'readable_name': 'num_returns_with_qualified_sick_and_family_leave_credit', '             description': 'Number of returns with qualified sick and family leave credit'},
    'A11450':     {'data_type': 'Double', 'readable_name': 'qualified_sick_and_family_leave_credit_amount', '                       description': 'Qualified sick and family leave credit amount'},
    'N10970':     {'data_type': 'Double', 'readable_name': 'num_returns_with_recovery_rebate_credit', '                             description': 'Number of returns with recovery rebate credit'},
    'A10970':     {'data_type': 'Double', 'readable_name': 'recovery_rebate_credit_amount', '                                       description': 'Recovery rebate credit amount'},
    'N10971':     {'data_type': 'Double', 'readable_name': 'num_returns_with_economic_impact_payment_first_round', '                description': 'Number of returns with economic impact payment first round'},
    'A10971':     {'data_type': 'Double', 'readable_name': 'economic_impact_payment_first_round_amount', '                          description': 'Economic impact payment first round amount'},
    'N10973':     {'data_type': 'Double', 'readable_name': 'num_returns_with_economic_impact_payment_second_round', '               description': 'Number of returns with economic impact payment second round'},
    'A10973':     {'data_type': 'Double', 'readable_name': 'economic_impact_payment_second_round_amount', '                         description': 'Economic impact payment second round amount'},
    'N06500':     {'data_type': 'Double', 'readable_name': 'num_returns_with_income_tax_after_credits', '                           description': 'Number of returns with income tax after credits'},
    'A06500':     {'data_type': 'Double', 'readable_name': 'income_tax_after_credits_amount', '                                     description': 'Income tax after credits amount'},
    'N10300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_tax_liability', '                                      description': 'Number of returns with tax liability'},
    'A10300':     {'data_type': 'Double', 'readable_name': 'total_tax_liability_amount', '                                          description': 'Total tax liability amount'},
    'N85530':     {'data_type': 'Double', 'readable_name': 'num_returns_with_additional_medicare_tax', '                            description': 'Number of returns with additional Medicare tax'},
    'A85530':     {'data_type': 'Double', 'readable_name': 'additional_medicare_tax_amount', '                                      description': 'Additional Medicare tax amount'},
    'N85300':     {'data_type': 'Double', 'readable_name': 'num_returns_with_net_investment_income_tax', '                          description': 'Number of returns with net investment income tax'},
    'A85300':     {'data_type': 'Double', 'readable_name': 'net_investment_income_tax_amount', '                                    description': 'Net investment income tax amount'},
    'N11901':     {'data_type': 'Double', 'readable_name': 'num_returns_with_tax_due_at_time_of_filing', '                          description': 'Number of returns with tax due at time of filing'},
    'A11901':     {'data_type': 'Double', 'readable_name': 'tax_due_at_time_of_filing_amount', '                                    description': 'Tax due at time of filing amount'},
    'N11900':     {'data_type': 'Double', 'readable_name': 'num_returns_with_total_overpayments', '                                 description': 'Number of returns with total overpayments'},
    'A11900':     {'data_type': 'Double', 'readable_name': 'total_overpayments_amount', '                                           description': 'Total overpayments amount'},
    'N11902':     {'data_type': 'Double', 'readable_name': 'num_returns_with_overpayments_refunded', '                              description': 'Number of returns with overpayments refunded'},
    'A11902':     {'data_type': 'Double', 'readable_name': 'overpayments_refunded_amount', '                                        description': 'Overpayments refunded amount'},
    'N12000':     {'data_type': 'Double', 'readable_name': 'num_returns_with_credit_to_next_year_estimated_tax', '                  description': 'Number of returns with credit to next year’s estimated tax'},
    'A12000':     {'data_type': 'Double', 'readable_name': 'credited_to_next_year_estimated_tax_amount', '                          description': 'Credited to next year’s estimated tax amount'}
}
