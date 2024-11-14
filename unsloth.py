from datasets import load_dataset

ds = load_dataset("qq8933/OpenLongCoT-Pretrain")

unsloth_template = f"""
Dame el resultado del siguiente problema o la cadena de pensamientos que llegaron a esa respuesta:
    Problema: {}


"""


def prompting(examples):
    sys="{SYSTEM} Eres un asistente matemático de nivel de ingeniería civil en informática y debes resolver el siguiente problema"

    examples
    user="{INPUT}"
    
    respuesta="{OUTPUT}"

    preCoT="""
