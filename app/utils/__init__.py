from .upload import upload_data_with_zip, upload_data_with_streaming, storage

prod_json = {
    "type": "service_account",
    "project_id": "clture-production",
    "private_key_id": "de5932a4a7de2f150f0f46341fd65b2175f5249f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9sS+a/stmpFlw\niwk9y/AwwCtRP9Os1zyNWRblO455oAoSMXiNp/paCYTyl2e7EVpOkoRkbfg5pV6s\nnEFffEpHiM/XraN9PUtyS6XXxOy8o/QYnIhLlND/qYV/kWJNcIxGYyWB30O+dSrO\n8CEozR3dXZS16prhj+dZVvg3MAyBu8Kp31WkzC/lvDn3oZtrENDA348XLesce2rx\ntsIJeudDC0RpI/vlKJAlkOff1BS+tc8N1UdjKrQUL3/+UBeYVRk/dYiHTxEH01Jx\nLpkwlV8W2OrFueq8x5boHeh9g5UZTmVcPfX8yPS5xwPrlJ+hD4sxrtU5D6piSlup\nxpnyR8uXAgMBAAECggEAC8+K78Mahf8IpJW7kxHuGBL2/32SX+oc1o4r+0Tch50b\n02sqHuPNFisOkI41wrN/ZHIB9UDVmj0+KlAmT9wswcx2aG7ixYr59hlYr5kOxmYM\n7jVc1RvkcW6sJbe3H6w4x68nqDDvBl5ENpND9UbkK6LGfhcn4pBzrp/YH5OJy8/5\n9E3uqAainrxeYYMkricmuR+osEW70L1/cmyyQFnrFbla9w3hx0O47h/y8rNvxWcL\nIyW1F0LcFT1lsFz9+DEjjgW9XWFVl9FgyX74a23LTjf0BC8nCcwliOfIeQe75O59\nQHqkb1Wb9SRoT2qhc07I1bvCRMmmaa+972c8W88coQKBgQDu8X2g53X1sJtVG7M/\ntyx97LSAlOj459aM6uy1Sn63dmEtQOT1Q6W3kBPhfFiieG03ufXST8lepBEM0OA+\nAD+y5JPyjQK1D7s76HCyrWjTxnzbJQtc5gNmQjf3Tuj+A0DDjEE55feQmY/5OnwD\naulH2nAwqTpjTnuzCr86S1uH4QKBgQDLO6q0FV7YOEQdHFRbbuQsqszeRKJ7afuG\n+7UFj0M9p89YOLlv5SRZ7Tv2MWTEwMI0gRW92mLpdexj0mTBhdH5FnKUPrNwQU96\ng5zPzspgdqUCic2wcRa7S2EqgR84yAvtOYyw7F+RL9hXtobRGl+YmY1gzXJD82TI\nGzTvmafidwKBgQDN52ZF8Q+Sf/TrO2qU3mlFvmOxZiD41PfrCUqf0yktOaL2FzT2\nMawtacfoCHpsz2/2lJZD/KNfnexfaePDKf26UAU5/8+0bXEAaAYtwwdRb3sKcXrA\nPCnzxd5qjCJ1OiJmIIfYt9ZFUj9iGsbhPxD17UO+eyYoi2pHWFx/hI7EoQKBgDlQ\nQFm81RyA8aSMArYuVabLHC9qh6/qOYbdoTVKK5pNosmsZY9Kva+mmYxabaKXAa2w\n4aLC3bYdDWcxRDzXMlnenL112UDFClbwmt534NbHXs2SczFZEyIKpgJIm7d1ovdp\njWWvo1vcdFR4IxkBKQht9VLhXWIQV9Ge6pTPbmsNAoGACety0/g1R/heNf4DwQ0o\n6891bkxd7MKFjTLHisouPCbAVeECJ4UF5U2WwEZko8taX5ssF5JBy9PJpM87WjPF\nGDhxg7ddiF9NFNYpdLvli0tjBm4Vcpxx5qiHuazb+exZ9+20QX3qfLN5nbTMSyWT\nHDeCfhYNJ/1NYMEd665G7O0=\n-----END PRIVATE KEY-----\n",
    "client_email": "clture-production-cluster-sql@clture-production.iam.gserviceaccount.com",
    "client_id": "115022260086442326358",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/clture-production-cluster-sql%40clture-production.iam.gserviceaccount.com"
}

# client = storage.Client.from_service_account_json('./app/prod.json')
client = storage.Client.from_service_account_info(info=prod_json)
