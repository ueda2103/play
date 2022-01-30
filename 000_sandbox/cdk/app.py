#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkVpcStack


app = cdk.App()
CdkVpcStack(app, "CdkVpcStack",
    env=cdk.Environment(account='787722544587', region='ap-northeast-1')
)

app.synth()
