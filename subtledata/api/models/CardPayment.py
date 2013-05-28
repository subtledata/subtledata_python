#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class CardPayment:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'name_on_card': 'str',
            'tip_amount': 'float',
            'expiration_year': 'str',
            'amount_before_tip': 'float',
            'tip_type': 'int',
            'card_id': 'int',
            'expiration_month': 'str',
            'mag_track_2': 'str',
            'mag_track_1': 'str',
            'signature_image': 'str',
            'tender_type_id': 'int',
            'billing_zip': 'str',
            'card_number': 'str'

        }


        #Name on card
        self.name_on_card = None # str
        #Payment Tip Amount
        self.tip_amount = None # float
        #Expration Year
        self.expiration_year = None # str
        #Payment Amount Before Tip
        self.amount_before_tip = None # float
        #Pass tip ID or use 0 to specify tip
        self.tip_type = None # int
        #SubtleData Credit or Gift Card ID
        self.card_id = None # int
        #Expration Month
        self.expiration_month = None # str
        #Mag Track 2 Data
        self.mag_track_2 = None # str
        #Mag Track 1 Data
        self.mag_track_1 = None # str
        #Signature Image in Base64
        self.signature_image = None # str
        #tender_type_id
        self.tender_type_id = None # int
        #Billing Zip Code
        self.billing_zip = None # str
        #CC Number
        self.card_number = None # str
        