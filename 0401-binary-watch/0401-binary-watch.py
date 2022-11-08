class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
    
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2 ,1]
        answer = defaultdict(set)
        
        def hour_backtrack(turnedOn, total_hours, index):
            if total_hours > 11:
                return
            if turnedOn < 0:
                return 
            
            minutes_backtrack(turnedOn, total_hours, 0, 0)
            for curr in range(index, len(hours)):
                hour_backtrack(turnedOn - 1, total_hours + hours[curr], curr + 1)
            
        def minutes_backtrack(turnedOn, total_hours, total_minutes, index):
            if total_minutes > 59:
                return
            if turnedOn == 0:
                answer[total_hours].add(total_minutes)
                return
            if index == len(minutes):
                return
            
            for curr in range(index, len(minutes)):
                minutes_backtrack(turnedOn - 1, total_hours, total_minutes + minutes[curr], curr + 1)
                
        hour_backtrack(turnedOn, 0, 0)
        result = []
        for hour in answer:
            for minute in answer[hour]:
                hour = str(hour)
                if minute // 10 == 0:
                    way = hour + ":" + "0" + str(minute)
                else:
                    way = hour + ":" + str(minute)
                result.append(way)
        return result
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            