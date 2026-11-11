import os
from twtags_safelist import (get_csr_components, 
                             get_twtags_safelist
                             )
from svelte_bundler import build_ssr_style_css
from svelte_bundler.csr import  build_csr_svelte_bundle


import logging

if os:
    try:
        os.remove("app.log")
    except:
        pass

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"    
logging.basicConfig(filename="app.log", level=logging.ERROR, format=FORMAT)      
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


#target_module = "demo_forms_and_input"
target_module = "demo_accordion"
#target_module = "demo_slider"
#print(get_csr_components(target_module))
build_csr_svelte_bundle(target_module,
                        enable_skui_theme_selector=True,
                        deploy_websocket_manager=False,
                        enable_inbrowser_exec=False)
