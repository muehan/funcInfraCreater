import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    locations = ["eastus","eastus2","southcentralus","westus2","westus3","australiaeast","southeastasia","northeurope","swedencentral","uksouth","westeurope","centralus","southafricanorth","centralindia","eastasia","japaneast","koreacentral","canadacentral","francecentral","germanywestcentral","norwayeast","switzerlandnorth","uaenorth","brazilsouth","eastus2euap","qatarcentral","centralusstage","eastusstage","eastus2stage","northcentralusstage","southcentralusstage","westusstage","westus2stage","asia","asiapacific","australia","brazil","canada","europe","france","germany","global","india","japan","korea","norway","singapore","southafrica","switzerland","uae","uk","unitedstates","unitedstateseuap","eastasiastage","southeastasiastage","eastusstg","northcentralus","westus","jioindiawest","centraluseuap","westcentralus","southafricawest","australiacentral","australiacentral2","australiasoutheast","japanwest","jioindiacentral","koreasouth","southindia","westindia","canadaeast","francesouth","germanynorth","norwaywest","switzerlandwest","ukwest","uaecentral","brazilsoutheast"]

    location = req.params.get('location')

    if location in locations:
        return func.HttpResponse(True)
    else:
        return func.HttpResponse(False)