import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJztO0lsHFd2v7rZzV4pklooai1tFCWZvXETbdO2RGoby5LSpIceykpPses3u5pdVa361SJpUEFm5ASDHMYZjIEkE+cQBAiQU3LIwRMgwSCHXHNKDsEEAXzLIcDcc0jee79+L2RzcTDJKSS7+tdf33v//bd+llnw0wefD+AjtkKMmfCnsTpjq62yxlY1VQ6x1ZAqh9lqWJX72GqfKkfYakSVo2w1qsr9bLVflWNsNabKcbYaV+UEW02ocpKtJlU5xVZTVA6xeprZA2x1gGn4Hmb1Y8weZKuD8r0P+9pDbHWIaXyYcY290aCksdpxZkbkS4rVhtgbQPEE4ydY7STjp2QDvIwwbD7NaqPYwwTg+6FN08zrbF3D7qUzzEywz2H0WWYmqXCOmSkqnGdmmgoXmAkgXmTmMXrVmQkQXmLrUL6MT+MKPa9SzTV6jjEToL7OzGG2Os44Y7UbzDxOcJkn2IOH5kl8nMLHCFu9yczTbPUWM0fZ6ltsa5vxt7C8EWJeLsQnmHkGR65mGIe/m1R/lurPUn2Wcfi7RfXRkHkOu43AzOdxtpcTIfMCrBPAcJFgePm1Zuo9KlfMS4RijpmXqZBn5hUqFJh5lQqTzLxGhSnGp5k5Rqv6IZ5DCmsObfDS+DhwoPVf8PNkXIOin4DHctXjhvnMdeuy7hg8FlzH4WXfcp17nud6sqEfHnc9d1Nwz0d2bvqV234MCraxVfItm1vYTeCcH0OfiTvr3PFFEV6fNrhnZOcyt3P6+B3H9FzLfEenSv0jy7Gyk4VMLlMoTE9lb09n9I/f0S3zhv7M48J3s4VMvpCZKkzq3+WeAICy8JqfKatzhUsu4LKnGOH44KEPxANODBHiwK1L43Di2BPqcPZ5/p25Gfv5pRc6FfP2vS3LHw8jetjLFT6WxbYgDDk24irth4jDY6lpG56nP1r0o/C2wetNwzuOjX0EUkQra8GRjynwliR4rzU8Xa9DbOttBoAuviiw12G2E8IztqMxnwCH8+XTK2w/HKfTb0JsdGQnzEZmYeDL42wFgIMhb3BHEYAntDVG1Tc/q5V9BMHH9S9ZWKRNGY+oyi0C2TMc07VpGBYtxye867Bh2LPMfWNjvE+NWaPnJj1Nelr7EgQHGWVj47RiBaZF4Tet5SRRcPp+RZTfahFl6w7iu/hiDmkDpRoLMETq9OGGAtmg5hTQyScKIT2g/RQQ53Ufe5lmK9APqDULb8GIKAkjagf0alAZwSYQNiN04pE3cIOeFBEHgRS4dE2IfmKUa+KdvG1dVLt69nnOFsgil3IC8UgQ5YlalmPyLUlL3qgbQDziId8rUpcovZhu06fem57lc9qP4hA+hvFxQpG6VkwdwG7FQXjTsXogoGxaO6aNawltWFIXAQwr6uJj6122QzQeWXyRQ0K3TodkLy14D9Np8YlEZkjKnSRbIRKF6fgQ0us/+yP8+fn7hD3hVxzFxxlFjEq9KarEBSgRqErUOW/QISQUP6Mn35eDcEjNqBvOTWyLEaJD2iCgKmIwSULX9VKPT+9q6J3VP93z0XtXJ/Rx/Vd/8vs/1Xfw6yfy60fy64fy6/f0G7rs9UVXrx93ff2OfgNW/rSU3fPRe1cnEoE8mj/aTyKQZHeaftX1dCnNJu23ZaFg37WcbcO2HNXve25zubnG9/Rb9qzyBoha162org8s/2Fzbe+UVd9viLez2XXLrzbXMmXXzqpVJtYsx7HUBHfr7vo69/adwMc1G7hkZg26iobr42zfkgKkAbr4/b6UJiYJ0/Uwew3sn0P2X3wxToK3D5l+5EGXgpCCITBaXp4KWJ6kKp37DGyYLGRahYwurkMhrbTJN3/wxQuF7ZLlrMOfbjmyZtZuC+CO83IOH+fxcQFbQ+r4+JZvbdABcfc9IKStrI332xL2GByOGEszEvgiTeJqMm8/cX39u826Q+OhpmDjm5TwdW544h5rqUT9iGTv/SNyWjDT/3PwkSlA5Fdr/E8pTz9kha0FqJBR14ZQymKvyUW+vdvPv/nD322xLBprjmFz/WlFXwYzUA86vQc/+r6jnhlCbLqe2XsU6oPHSEQTT4JolstciEqzXt/WDaFLTWHUBSdFtuK5cGLUhKKEestcn3Ab3NEPIXm2kCvksrlC1uGbEz737ObWBFTbYNSIiYrrTVRAH6+57sYEdsxUfbv+vj2f71hWYU/yJAmfqJInfw+nUsoKU+rK7TNke5B8QbOCoVmBQmTF+TLUB4QGvCohtpFg3t+GwJ3pGgx2ANj+JGpOQAHfwGYgx4f0MpRjVA4x2E6cdXuI+XGyB+M0w4qjsz7Y3VqSlvhLhh5TAudJSSNfY5/4aRozwErHqDCI7pOJ7ZqG9mUcvTLwn94FWyp4GWDvYmlYisM4+nBQArsL/CowsjaizCuFtjMaeFcoPsGBGoHBI+BCjYBhZSXRgQLnaQZ8J/CcZqAPzD8D/hM4TzPgLoGXRF9n4QucuPPwdQF9mxm0ek/CGzhul+DrMvo0M68jzCd3EfwapEaU7URZ7RTabUgDfBkh+PrZTgQbQLzu9KPzM0M23RhC7pNrCcCDQ7mDol17HWP+GVY7y3ZirHaOZo6rzRynzUywHSDtebYDbvINNkqLQcUF6UbcbDkW5i25nbAEuJ5vqf5kUSp2eFkCdoAOOqtdor16Htq1V9DjE3TKJhSJvwyZmfYaWbnGZVa7wsycfAkG/l3IzB/c8WqLG0iXFcjCvab0CBwey8n4Wz5pGc9qWVnB+Z0XU/uc+MdPHzx6oq88Wn6o37+zcO/u06cf6p39xK2Ogbdawx4tZu/ZhlVXHldLmu7TvyVY9vRHD07JAzujTjaKAYFIKund4d0tV7nHdUvojgtyCOSDw3293HJuyedzPFKbJJM4AkoSswFQCBQHwnjFJ0z+ygIJ9gDejYZV2uDb87dvF4zbU3O5yZm8aczdns0V1ipzs0aukDfNcn7KLHvcBHfKAilX8rcbfL4R4EVrzIvvowh0Pdvw57+z9PQJ+MrgDvu8ZBvlquXwkmXO51uVICjR9y2VAV+Li/l83S0bdT7PndLHS2BmV11z3gBFmqHdVSvNi3fIKfGbnlMSol4Cj9pteoDIfO7VfD6TmylUbpf5XGV2ai0PxalyvjBZLhcmpyZnjSljsuCjr3EYotL5lFQhRaSW99Fb2U0GIi4iTH6RJABxYt5HD7oHGfzTnfW7KCF3DalA80mykFXUJge1SCLRSjn/xD5kIRcQ6ELdXpGhZZvT0p2z1snoU/wHCHdxYBajFaBKXnEv06g2aM2G4Rm2IA/PR7fOIC1Y8t0N7ohrnRz7zVc/faHY/DHCrC+1VKa400sfbm5uZrbBpwSTiJYvVw3g6nr244VHC7n84+1HT6dd0Jb533Bn7ltTH22KjzqAX/eMRrUbfJtnK57FQW2+H/BTwxX+WNMyxfz6pmU3hTE51onAPNkZ5SoHtewCkcV7vY/gI18XnNug9KuGrwPIng7TuE3H16tgChh6xxTIMJ6tT3gVvSWmZFDpZu/JlawIJAwc9E1U6uNI3CLZ0+R9bwuf28R5SEMq2NxpErd+yLcpxkVs/OipLPdJQen6KDE9Y7MEh6rpF6+yIE605lELWA1AduszTjN9XHxMo4v4QlMsg9lFTSWgte9627SIJUpoh/gkXXgdRFEJzwGNoALB3FyzLZ+K68ipdRoKFKvWrTXiSLB4qLnZMOFgEDxVvmVa68CItKjHXzaRKak3TEIL1IQrPYC6a5gyyuXzLb/twJfrrpCnFBmANplvlXkD5aUoal1+SzAR7NR4suXBAHP4RCQ4urhyY1N+Aw7F9xRlAGSDQh101Iwi7m8Rgy2EZtOxNrgn9g2DoIVYw2p8MHB+wuACJbXjUIpocfik4LcfajFuEIGWFMUP0lqCWsLaKW2JnKaUdkKLaie1YXgbgtYI1J2kmSLaALRG5KiQ/CYTMRJ8yESsaLtNxNEuE1HGVcBQXHEWGVqIaAzU2W7bEMzClkaXniiQshbFCBa99Lc0+vY8Woe1OBqO4NmOBMYjGYUYNksFJiTaVjE2GsQW41DqAxgqAEOaYPjVXhgSR4LhCkwRQwOzdowmGtbQskni2MG2Fdpl+A6h4ZtCqxAN3wGK3IFtiaHwQbTryKTs7DKMA47jlMPtIO6JfcwYYh1xkfUK7i6joALF/8qogxzbX7rcOkw2vt8t+ZCD0WcoGjh6vufa30bu5XtDf7Dx0sNym+2YJ4g+gGYJal4E9pX+BH29nsZVMEbv/jnitI8WdX3vtCf3m5b0RdesBTu/e84l3/B8/aFR3sCYygr47XqHvy9yu6fI27muKfK2jgH+znXHjyvdULyLjwUlkjALUrzfJd9I0BRX8PEJPr6Hj1V8PMcH+u/F38QHiUXciuIDJQcbVt2qyrDP9xl5iqB9/M0iV+sBAxnEQPuKuUV4+zOs/qAl5kZJEElxlIT34yC6EiCq2rUJEl7JQBRiDQrEiBReKkZMwuszRsJLHlOQUTuU+cO80XUUX3D8NHmin1JTHzXNo3yj2jmqjVBtDfFTkkIGkfuV10udU10ztiPvAo91QjEIhg6CchEVj7jS82Dct+p1DCuUXc+Ds1DfLqLLUnybBcEveeyL3HZf8d7Hfhy1TPEhPiy1YaLZ4F7xUjd3IJCU/SpWDtopnOQfsPo0UTlFqgOVjfxIFdLKWbXUx8/YUdSHgaJ7FuRuhCRuifz+vRoDPOP+1h7E9pHFcRStFGpAQUtvKPdJgIMAhjkT7R1K/++J3B7Ca+YI8mDBA1Gg3/dcGx5oreqPLbBwCnuHFg4dKkR277DJg4ZZ4FpcPYLIuQtDyCDaJWaKVSUNesoZEh1JJTpKxI8HZh+LdXj7Z6zWsTGkBIQSD8oairQFwEAn+30QPqIAmAy1BcCfI4cCYyq2Q0aUGXzgKGBRGcVS7BhHc0VZKXFWS5CVkgyslK1/0dA8SbDRxRcjFLhJsVqaAjdJGYJ5+SPg/b/WcPkULf+n2kHLMzQhcO4+tv0eC2AYkEYGWBwKloiCJaJgieLlgZ0oXg8YBVtkxbkO522AztsHZOEMy/MWXBbwj7XPVwSjXx0oB8udbC/XE/V/Y52o9yvU+9uov9FWnJ/Tppwi1G+HDkB9e4G2coSmj2HiA+yxnRgG4VCQ0FWMxRejFPaSK6mYH631H9rKysvVUB844YjzFMWrRgOcz3TiDL0+cS4TWGcJrCch8Kd7CflzzD/J/FO43htisRHJIOelvUlBQFOnTE2CMjUJmalJYjxwJ4mZmpH2LRFNxu/MyxLgL0IrD80rnRSQFyFep5h/DsOBSAfAMk0xvRQBEYJVW73HcOx1BeIFBaI5Dvsm6y62wTZvdG//ibaQvPnrVmPXeovHGx1zfPPV37TCZQ/A20LjCMyvYM1MJiMm2VG9/S7LtmgiBGiUkF9W6IoFtkN099AaDcToddFaumX3zdri7MEAUAC+e+0uO3qvmanWJusV3HnDUeL2bUX34voBxJbqAlNi98EINy+Jc6wjpBBMgZJbLUgxh4MpLjpJjgZ0b6oSLSdpT/alJegW/ZkB9u0eUkptq+/HQryNk7jQiZLegZOK076QRtJbPSFZdn2j3saqczev70MKss+RFh10OCBrihRI79nir3dvMencjlmlkzbXgwIINDgJbgMdAqQ43RoS+sJy8bEO/pMTvH9GtyOU8sO7OGIpSgoPhDPmWTqNpBVnCIS/zOPcRGOLHO8z0SBVHJJpEHBiQZiNBBkbEv0g0Gux4NIKaEu8dkJyHwQ2DYmyEVIN/S0tFCW/PaJUUAxVEGYDfoGak8Yk5BhKHKDU1ki7IJjO5xFQFaizUmwUB13XzPTuQQOoj0D1YYajH7ULuO2YoRkMQBmSc2GDdN/BW9+1zPkI6uNhNgrCbwTzKHtwih0Jpy+1Tpxi3TjFgsX+qq8bp//swil2KE6xg3FSyzzqUzidAJziPXCKHwmnaqgTp3g3TvFgsV+Gu3H6x1AnTvFDcYofjJNaphkGmwM06V5cEkfCZSrciUuiG5dEsMjgLlz+ONyJS+JQXBIH46KW+YuQ2p9TsD/JHjglj4RTrK8Tp2Q3TslgsXdD3Ti5fZ04JQ/FKXkwTmqZf9IUTiOAU6oHTqkj4fTLLpxS3TilgsWqWjdOC5FOnFKH4pQ6GCe1jKZ9K6GoCHAaCJDuQYD0kQjwr5FOAqS7CZAOIFtn3QRYjHYSIH0oAdIHE0Atg5HdfqUjyB7E6z1PZLSn6R9qBuFl2+wuawGD+rO3Z+BP/KRj+NrEnpyTzNRk26mu7pkKk7Oz03NzubnpufzM9PS1wnRhenYhV8lP5QxjjZuVtZlpo1yYNWYn57iZNwqFmcm1/FiQlcRMwZgwN0qv5MXb+cJYkLocAajGOjOQY+2MI8ZUcNS85Yqx/fOXY8Jan5+sTE9PV+bmAI58pWzOGkauPDVVmb5dmS4UeGWm+AEq6k7DN/DS28mxLtcbTECBdyqVtbPTqsU4BGbMOqlHGROOCZuSLdb3LgN2SCtCu2eZYbm/2XYQlwIjXFnOO/K+JKVPKpYn/BLGiynOlC9MTsmcIpQoUfPM2LCEb8h0dL5A0UHsJQv5QmF8WAUTaAZ7w7Rkvurpksw4tUOUFF3ojlPKLJFXx8RRvyy20mCYBZLMuiGon9GAJlOGKzAnVPwUZ0Aoy1wiOo5mFI0xvHV5EVxwj1CnG60y+gkMkSdvgsjxkvrDDK3GQqs02SpNtUrTrdJMqzR74J1j4EznGiwlfkGhkCglf9JaH3yf1Ya1qHZRO6aloO5EaBCex7RRLQHlgW9Z/+uaB2Hq3XY6HNYsNOTpKB3mDxVsZfg+NIR+l4PFu+DajTr3udlhlGfEdA+TvxCY/E8/zCqOf7Y3gn+MtSL4qpv4sOdsMJockhYoS8Yrvvsex6y999yMo3cjw7E26wqbYUxMxmQPZHFyWYs/YCooj4ExGdmnBC43zLrlBLcFhO9ZDRmAwwB7EUO2RURy3+uZ+C8MkuNto1H8baz5IbIiHQTKlHJjoyOFSe4K9bdMebG+5m7I/y9oyKveUWqrw6mXpxCAK17G8ei8Fn+sJmnsG/lDMv07Vn+OjR0BZxnzS1BiYEg73apJBQdhiN4TWhI+Z3f1CUPpHNTKHpj/xLB1f+gkvKkrpkOg66BvOO5hThWjizeot0xzl/AYlkp0n/X/5h9BxmdaDBNVm0awUFLcsnkRo9hFdPloBzyZKffpn17Ax5SM9FqxilRQICklv30H63HH7GbdtxryqMGoTMN165ItjrN2pj2zO1MeUpvtcZK0KMcF901eMWBC7pRdguERdhuSbaWq4Zh1XvLcNdeXHHsfb0qqsa12XgG6VKlDCW0EgvPh8vKzomwJBIPrkRIyTLMKGAPpZJ4K83L07wTydNE5u6r4eQ38b3mnlHtVQ1h14nfJ+YYiMHLvuteUV11eNeuOK5kZi3R4g/8kouCWumXZWacubwSKCM7GQzV3M+hexAyfjI7TWbVah9tWXUukWYHnWkell4rAnu/artms8/dICKAQ+Qo4GH7DCboJkAbeT4XjkXgsnogfj4bi0ajW9RuCcxGNaJEQlqMkuuVvXIvDORmEz1AoPhe/Eh+MH49/ndL+GxZlmgg="))))