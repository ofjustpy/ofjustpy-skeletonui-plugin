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

#target_module = "td_render_styeditor"
target_module = "demo_forms_and_input"
build_csr_svelte_bundle(target_module,
                        enable_skui_theme_selector=True,
                        deploy_websocket_manager=True,
                        enable_inbrowser_exec=False)

