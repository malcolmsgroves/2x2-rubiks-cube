import imagematrix
import numpy

class ResizeableImage(imagematrix.ImageMatrix):
    
    
    
    
    def best_seam(self):   
        
        
        dp = {}
        energy = {}
        parent = {}
        
        for y in range(self.height):
            for x in range(self.width):
                energy[(x, y)] = self.energy(x, y)
        
        for x in range(self.width):
            dp[(x, 0)] = energy[(x, 0)]
            parent[(x, 0)] = None
            
            
            
        
        for y in range(1, self.height):
            for x in range(self.width):
                
                dp[(x, y)] = dp[(x, y - 1)]
                parent[(x, y)] = (x, y - 1)
                
                if x != 0:
                    if dp[(x, y)] > dp[(x - 1, y - 1)]:
                        dp[(x, y)] = dp[(x - 1, y - 1)]
                        parent[(x, y)] = (x - 1, y - 1)
                
                if x != self.width - 1:
                    if dp[(x, y)] > dp[(x + 1, y - 1)]:
                        dp[(x, y)] = dp[(x + 1, y - 1)]  
                        parent[(x, y)] = (x + 1, y - 1)
                        
                
                dp[(x, y)] += energy[(x, y)]
                
        
        # find minimum
        index = 0
        
        
        # need parent node and 
        for x in range(1, self.width):
            if dp[(x, self.height - 1)] < dp[(index, self.height - 1)]:
                index = x
        
        min_seam = [(index, self.height - 1)]
        
        
        
        for row in range(1, self.height):    
            
            min_seam.insert(0, parent[min_seam[0]])
            
            
        
        return min_seam
                
        
                
                
                    
                

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())





