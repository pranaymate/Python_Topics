_____ m.. _______ P..
_______ m..
_______ qu..
_______ ti..

___ myTask(queue):
  value = queue.get()
  print("Process {} Popped {} from the shared Queue".format(multiprocessing.current_process().pid, value))
  queue.task_done()

___ main():
  m = multiprocessing.Manager()
  sharedQueue = m.Queue()
  sharedQueue.put(2)
  sharedQueue.put(3)
  sharedQueue.put(4)

  process1 = multiprocessing.Process(target=myTask, args=(sharedQueue,))
  process1.start()

  process2 = multiprocessing.Process(target=myTask, args=(sharedQueue,))
  process2.start()
  
  process3 = multiprocessing.Process(target=myTask, args=(sharedQueue,))
  process3.start()
  
  process2.join()
  process1.join()
  process3.join()

if __name__ == '__main__':
  main()