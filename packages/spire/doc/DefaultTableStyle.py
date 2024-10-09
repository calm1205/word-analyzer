from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DefaultTableStyle(Enum):
    """
    Enum class representing default table styles.
    """

    TableNormal = 105
    TableGrid = 154
    LightShading = 158
    LightShadingAccent1 = 172
    LightShadingAccent2 = 190
    LightShadingAccent3 = 204
    LightShadingAccent4 = 218
    LightShadingAccent5 = 232
    LightShadingAccent6 = 246
    LightList = 159
    LightListAccent1 = 173
    LightListAccent2 = 191
    LightListAccent3 = 205
    LightListAccent4 = 219
    LightListAccent5 = 233
    LightListAccent6 = 247
    LightGrid = 160
    LightGridAccent1 = 174
    LightGridAccent2 = 192
    LightGridAccent3 = 206
    LightGridAccent4 = 220
    LightGridAccent5 = 234
    LightGridAccent6 = 248
    MediumShading1 = 161
    MediumShading1Accent1 = 175
    MediumShading1Accent2 = 193
    MediumShading1Accent3 = 207
    MediumShading1Accent4 = 221
    MediumShading1Accent5 = 235
    MediumShading1Accent6 = 249
    MediumShading2 = 162
    MediumShading2Accent1 = 176
    MediumShading2Accent2 = 194
    MediumShading2Accent3 = 208
    MediumShading2Accent4 = 222
    MediumShading2Accent5 = 236
    MediumShading2Accent6 = 250
    MediumList1 = 163
    MediumList1Accent1 = 177
    MediumList1Accent2 = 195
    MediumList1Accent3 = 209
    MediumList1Accent4 = 223
    MediumList1Accent5 = 237
    MediumList1Accent6 = 251
    MediumList2 = 164
    MediumList2Accent1 = 182
    MediumList2Accent2 = 196
    MediumList2Accent3 = 210
    MediumList2Accent4 = 224
    MediumList2Accent5 = 238
    MediumList2Accent6 = 252
    MediumGrid1 = 165
    MediumGrid1Accent1 = 183
    MediumGrid1Accent2 = 197
    MediumGrid1Accent3 = 211
    MediumGrid1Accent4 = 225
    MediumGrid1Accent5 = 239
    MediumGrid1Accent6 = 253
    MediumGrid2 = 166
    MediumGrid2Accent1 = 184
    MediumGrid2Accent2 = 198
    MediumGrid2Accent3 = 212
    MediumGrid2Accent4 = 226
    MediumGrid2Accent5 = 240
    MediumGrid2Accent6 = 254
    MediumGrid3 = 167
    MediumGrid3Accent1 = 185
    MediumGrid3Accent2 = 199
    MediumGrid3Accent3 = 213
    MediumGrid3Accent4 = 227
    MediumGrid3Accent5 = 241
    MediumGrid3Accent6 = 255
    DarkList = 168
    DarkListAccent1 = 186
    DarkListAccent2 = 200
    DarkListAccent3 = 214
    DarkListAccent4 = 228
    DarkListAccent5 = 242
    DarkListAccent6 = 256
    ColorfulShading = 169
    ColorfulShadingAccent1 = 187
    ColorfulShadingAccent2 = 201
    ColorfulShadingAccent3 = 215
    ColorfulShadingAccent4 = 229
    ColorfulShadingAccent5 = 243
    ColorfulShadingAccent6 = 257
    ColorfulList = 170
    ColorfulListAccent1 = 188
    ColorfulListAccent2 = 202
    ColorfulListAccent3 = 216
    ColorfulListAccent4 = 230
    ColorfulListAccent5 = 244
    ColorfulListAccent6 = 258
    ColorfulGrid = 171
    ColorfulGridAccent1 = 189
    ColorfulGridAccent2 = 203
    ColorfulGridAccent3 = 217
    ColorfulGridAccent4 = 231
    ColorfulGridAccent5 = 245
    ColorfulGridAccent6 = 259
    Table3Deffects1 = 142
    Table3Deffects2 = 143
    Table3Deffects3 = 144
    TableClassic1 = 114
    TableClassic2 = 115
    TableClassic3 = 116
    TableClassic4 = 117
    TableColorful1 = 118
    TableColorful2 = 119
    TableColorful3 = 120
    TableColumns1 = 121
    TableColumns2 = 122
    TableColumns3 = 123
    TableColumns4 = 124
    TableColumns5 = 125
    TableContemporary = 145
    TableElegant = 146
    TableGrid1 = 126
    TableGrid2 = 127
    TableGrid3 = 128
    TableGrid4 = 129
    TableGrid5 = 130
    TableGrid6 = 131
    TableGrid7 = 132
    TableGrid8 = 133
    TableList1 = 134
    TableList2 = 135
    TableList3 = 136
    TableList4 = 137
    TableList5 = 138
    TableList6 = 139
    TableList7 = 140
    TableList8 = 141
    TableProfessional = 147
    TableSimple1 = 111
    TableSimple2 = 112
    TableSimple3 = 113
    TableSubtle1 = 148
    TableSubtle2 = 149
    TableTheme = 155
    TableWeb1 = 150
    TableWeb2 = 151
    TableWeb3 = 152
    PlainTable1 = 267
    PlainTable2 = 268
    PlainTable3 = 269
    PlainTable4 = 270
    PlainTable5 = 271
    TableGridLight = 272
    GridTable1Light = 273
    GridTable2 = 274
    GridTable3 = 275
    GridTable4 = 276
    GridTable5Dark = 277
    GridTable6Colorful = 278
    GridTable7Colorful = 279
    GridTable1LightAccent1 = 280
    GridTable2Accent1 = 281
    GridTable3Accent1 = 282
    GridTable4Accent1 = 283
    GridTable5DarkAccent1 = 284
    GridTable6ColorfulAccent1 = 285
    GridTable7ColorfulAccent1 = 286
    GridTable1LightAccent2 = 287
    GridTable2Accent2 = 288
    GridTable3Accent2 = 289
    GridTable4Accent2 = 290
    GridTable5DarkAccent2 = 291
    GridTable6ColorfulAccent2 = 292
    GridTable7ColorfulAccent2 = 293
    GridTable1LightAccent3 = 294
    GridTable2Accent3 = 295
    GridTable3Accent3 = 296
    GridTable4Accent3 = 297
    GridTable5DarkAccent3 = 298
    GridTable6ColorfulAccent3 = 299
    GridTable7ColorfulAccent3 = 300
    GridTable1LightAccent4 = 301
    GridTable2Accent4 = 302
    GridTable3Accent4 = 303
    GridTable4Accent4 = 304
    GridTable5DarkAccent4 = 305
    GridTable6ColorfulAccent4 = 306
    GridTable7ColorfulAccent4 = 307
    GridTable1LightAccent5 = 308
    GridTable2Accent5 = 309
    GridTable3Accent5 = 310
    GridTable4Accent5 = 311
    GridTable5DarkAccent5 = 312
    GridTable6ColorfulAccent5 = 313
    GridTable7ColorfulAccent5 = 314
    GridTable1LightAccent6 = 315
    GridTable2Accent6 = 316
    GridTable3Accent6 = 317
    GridTable4Accent6 = 318
    GridTable5DarkAccent6 = 319
    GridTable6ColorfulAccent6 = 320
    GridTable7ColorfulAccent6 = 321
    ListTable1Light = 322
    ListTable2 = 323
    ListTable3 = 324
    ListTable4 = 325
    ListTable5Dark = 326
    ListTable6Colorful = 327
    ListTable7Colorful = 328
    ListTable1LightAccent1 = 329
    ListTable2Accent1 = 330
    ListTable3Accent1 = 331
    ListTable4Accent1 = 332
    ListTable5DarkAccent1 = 333
    ListTable6ColorfulAccent1 = 334
    ListTable7ColorfulAccent1 = 335
    ListTable1LightAccent2 = 336
    ListTable2Accent2 = 337
    ListTable3Accent2 = 338
    ListTable4Accent2 = 339
    ListTable5DarkAccent2 = 340
    ListTable6ColorfulAccent2 = 341
    ListTable7ColorfulAccent2 = 342
    ListTable1LightAccent3 = 343
    ListTable2Accent3 = 344
    ListTable3Accent3 = 345
    ListTable4Accent3 = 346
    ListTable5DarkAccent3 = 347
    ListTable6ColorfulAccent3 = 348
    ListTable7ColorfulAccent3 = 349
    ListTable1LightAccent4 = 350
    ListTable2Accent4 = 351
    ListTable3Accent4 = 352
    ListTable4Accent4 = 353
    ListTable5DarkAccent4 = 354
    ListTable6ColorfulAccent4 = 355
    ListTable7ColorfulAccent4 = 356
    ListTable1LightAccent5 = 357
    ListTable2Accent5 = 358
    ListTable3Accent5 = 359
    ListTable4Accent5 = 360
    ListTable5DarkAccent5 = 361
    ListTable6ColorfulAccent5 = 362
    ListTable7ColorfulAccent5 = 363
    ListTable1LightAccent6 = 364
    ListTable2Accent6 = 365
    ListTable3Accent6 = 366
    ListTable4Accent6 = 367
    ListTable5DarkAccent6 = 368
    ListTable6ColorfulAccent6 = 369
    ListTable7ColorfulAccent6 = 370

