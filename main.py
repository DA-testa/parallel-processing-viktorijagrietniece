# python3

def parallel_processing(n, m, data):
    output = []
    time = [0]*n
    
    for i in range(m):
        x = min(time)
        thread = time.index(x)
        start = time[thread]
        time[thread] = time[thread]+data[i]
        
        output.append((thread, start))

    return output

def main():
   
    data = list(map(int,input().split()))
    n = data[0]
    m = data[1]
    data = list(map(int,input().split()))
   
    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
