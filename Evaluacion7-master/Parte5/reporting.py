from time import sleep

def report_progress(futures, tag, callback):
    not_done = 1
    done = 0
    while not_done > 0:
        not_done = 0
        done = 0
        for fut in futures:
            if fut.done():
                done += 1
            else:
                not_done += 1
        sleep(0.5)
        if callback:
            callback(tag, done, not_done)
