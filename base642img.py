import base64
strs="/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/2wBDAQICAgICAgUDAwUKBwYHCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgr/wAARCAEsASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD7Yooor8XP7ICiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKs6fousau+zStJubps4xbwM5/QGmk5OyJlKMFeTsvMrUV1uj/AAH+M2vMF074Z6zhvuvcWTQqf+BSbR+tdhoX7Evxv1badRtdM0wHr9svwxH/AH6D110sux9b4KUn8n+tjycTxBkWD/jYqnH/ALfTf3JyZ5FRX034X/YB0mLbL4z8f3E396DTLVYwP+Bvuz/3yK89/ak/Z/s/g5qtjqnhZbh9Fv4/LDTvvaK4UcqTj+IfMPo3pXViMkzHC4Z16sbJeab+5Hm4DjPh7M8xjgsNVcpyvZ8rUXbWybtd2vbTWx5NRRRXkn1QUUUUAFFFFABRRXV/Bj4X6l8XPH1n4Sst6QE+bqFyo/1ECkbm+p4Ue7CtKVKpXqxpwV23ZGGKxNDBYadetK0IJtvsl/X32RylFfXHiL9hv4WTaFdx+GrjUodQNu32KS4vA0Ylx8u4beRnGfavk7U9NvtH1GfSdUtXgubWZoriGQYZHU4Kn3BFduYZXi8tcfbJe9s07o8bIeJ8q4jU/qjd4WupKz12drvTp6kFFFFecfQBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAV9HfsifBP4XfEf4aXmu+NfCcd9dxa3LAkz3EqERiKFguEYDqzH8a+ca+uP2Df8Akj2of9jHN/6It693hylSrZmo1Iprllo1fsfD+IeKxOD4alUoTcJc8FeLaerd9VY6r/hlP9n/AP6J1B/4G3H/AMco/wCGU/2f/wDonUH/AIG3H/xyvl/9pjUtRh+O3iSKG/mRRerhVlIA/dp712n7B99e3PxT1RLm8lkUeH3IDyEjPnw+te5RzHL6uZfVPqsV7zje0el9bcvkfFYvh/iDC8OvNf7TqO0FPlvPqo6X5/729uhnftjfDLwN8NNf0Wz8D6AlhHdWcr3CpM772DgA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ia0qtXCwlKTu24ptvuze8d/E/wAe/Ey9S+8b+JZ79os+TG+Fjjz12ooCr9QMmsGiiuWpUqVZuU2231ep6lChQw1JUqMVGK2SSSXyVkFFFFQahRRRQAUUUUAFa/gPxrq/w78W2fjPQY4Gu7FmaFblCyEsjIcgEE8Me9ZFFVCcqc1KLs1qjOtSpV6UqVRXjJNNPZp6NfM7/wCK/wC0d4/+MehQeHvFlrpqQW12LmM2du6NvCsvJZ24wxrgKKK0r4itianPVk5PuzDBYHB5dQVDC01CCbdltd79XuFFFFYnWereEv2xPit4M8M2PhTSLHRmttPtlggM1nIzlVGBkiQZP4V5U7mRzI3Vjk0lFdFbF4nERjGrNtR2v0/qyODB5Xl2X1KlTDUowlN3k0t3du71fVv7wooornO8KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/9k="
imgdata=base64.b64decode(strs)  
file=open('1.jpg','wb')  
file.write(imgdata)  
file.close()  