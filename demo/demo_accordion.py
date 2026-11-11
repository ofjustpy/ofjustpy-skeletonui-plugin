

import kavya as kv
import skeletonui_components as SKUI 
accord = kv.AD.SKUI.Accordion.Root(key="accord",
               childs = [kv.AD.SKUI.Accordion.Item(childs = [kv.AD.SKUI.Accordion.ItemTrigger(childs = [kv.PC.PlainText(text="Hello")]
                                                                        )],
                                        value=1
                                        )]
               )


wp_endpoint = kv.create_endpoint(key="demo_skui_accord",
                   childs = [accord],
                   skeleton_data_theme="mint",
                   svelte_bundle_dir="csr",
                   rendering_type="CSR"
                   )

app = kv.load_app()
kv.add_route("/", wp_endpoint)



