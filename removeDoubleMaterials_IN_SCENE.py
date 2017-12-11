import bpy

for o in bpy.context.scene.objects:
    
    if hasattr( o, 'material_slots'):
        
        for m in o.material_slots:
            
            if len(m.name.split('.')) > 1:
                if bpy.data.materials.__contains__(m.name.split('.')[0]):
                    o.material_slots[m.name].material = bpy.data.materials[ m.name.split('.')[0]]
                
            
                
    
    