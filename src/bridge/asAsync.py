import asyncio
import logging as l


class asAsync():
    def toAsync(kwargs):
        if kwargs == "run_all_selected":
            l.info("run current selected")

        if kwargs == ("obs_connect"):
            l.info("Obs Connect Button")
            asyncio.run(self.obsConnect())

        if kwargs == "toggle_rec":
            asyncio.run(self.toggle_rec())
            l.info("toggle_rec")