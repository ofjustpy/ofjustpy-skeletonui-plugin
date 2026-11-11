

import kavya as kv
import skeletonui_components as SKUI


# <Slider defaultValue={[50]}>
# 	<Slider.Label>Label</Slider.Label>
# 	<Slider.Control>
# 		<Slider.Track>
# 			<Slider.Range />
# 		</Slider.Track>
# 		<Slider.Thumb index={0}>
# 			<Slider.HiddenInput />
# 		</Slider.Thumb>
# 	</Slider.Control>
# 	<Slider.MarkerGroup>
# 		<Slider.Marker value={25} />
# 		<Slider.Marker value={50} />
# 		<Slider.Marker value={75} />
# 	</Slider.MarkerGroup>
# </Slider>

slider = kv.AD.SKUI.Slider.Root(key="slider", 
    default_value=[50],
    childs=[
        kv.AD.SKUI.Slider.Label(
            childs=[kv.PC.PlainText(text="Label")]
        ),
        kv.AD.SKUI.Slider.Control(
            childs=[
                kv.AD.SKUI.Slider.Track(
                    childs=[
                        kv.AD.SKUI.Slider.Range()
                    ]
                ),
                kv.AD.SKUI.Slider.Thumb(
                    index=0,
                    childs=[
                        kv.AD.SKUI.Slider.HiddenInput()
                    ]
                )
            ]
        ),
        kv.AD.SKUI.Slider.MarkerGroup(
            childs=[
                kv.AD.SKUI.Slider.Marker(value=25),
                kv.AD.SKUI.Slider.Marker(value=50),
                kv.AD.SKUI.Slider.Marker(value=75)
            ]
        )
    ]
)




wp_endpoint = kv.create_endpoint(key="demo_skui_accord",
                   childs = [slider],
                   skeleton_data_theme="mint",
                   svelte_bundle_dir="csr",
                   rendering_type="CSR"
                   )

app = kv.load_app()
kv.add_route("/", wp_endpoint)



