from addict_tracking_changes import Dict
import justpy as jp
from justpy import JustpyBaseComponent
from justpy import WebPage
from py_tailwind_utils import *
from dpath.util import get as dget, set as dset
import hjson
from ofjustpy.htmlcomponents import genStubFunc 
import ofjustpy  as oj
from py_tailwind_utils import dupdate

class ChartJSMixin(TR.DivMixin):
    vue_type = 'ChartJS'
    # chart_types = [] #TODO
    def __init__(self, chart_name, cjs_cfg,  **kwargs):
        super().__init__(**kwargs)
        

        self.cjs_cfg = cjs_cfg
        self.domDict.chart_name  = chart_name
        self.domDict.chart_type = cjs_cfg.chart_type
        self.domDict.chart_options = cjs_cfg.options
        self.domDict.chart_data = cjs_cfg.data
        self.domDict.canvas_id = "canvas_" + chart_name
        
        

        # TODO: the refactoring in htmlcomponents for classes is little off 

    def react(self, data):
        """
        called every time before object is rendered
        """
        pass
    def __repr__(self):
        return f'{self.__class__.__name__}( vue_type: {self.vue_type})'


    def update_chart(self, spath, value):
        assert False
        # we might have to update the domDict as well
        try:
            print (f"Updating chart for {spath}")
            dupdate(self.cjs_cfg, spath, value)
        except Exception as e:
            # uvicorn runtime without Crash can eat up exception
            print ("exception in chart_update ", e)
            raise e
                                 
        
    def convert_object_to_dict(self):
        #print ("chartJS: convert_object_to_dict: ",  chart_options)
        d = {}
        d['vue_type'] = self.vue_type
        # Add id if CSS transition is defined
        d['id'] = self.id

        d['chart_type'] = self.cjs_cfg.type
        
        d['chart_options'] = self.cjs_cfg.options
        
        d['chart_data'] =  self.cjs_cfg.data
        
        d['chart_name'] = self.chart_name

        d['canvas_id'] = "canvas_" + self.chart_name
        d['show'] = True

        d['events'] = self.events

        d['classes'] = self.classes
        d['style'] = self.style
        
        
        return d
    

