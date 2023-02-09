class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        hashmap = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12"
            
        }
        day = date[0][:-2] if len(date[0][:-2]) == 2 else '0'+date[0][:-2]
        month = hashmap[date[-2]]
        year = date[-1]
        return year + '-' + month + '-' + day
    
        
        
        
        