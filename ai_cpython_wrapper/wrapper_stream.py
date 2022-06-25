
'''
回调函数

@param
    type: str
    desc: 会话句柄
@param
    type:[{}]
	desc:	返回结果实体(对应ASE平台上的响应数据)
        key: 返回数据段的名称
        type: 返回的数据类型 0: 文本 1:音频 2:图像 3:视频 4:个性化数据
        stauts: 数据状态 非流式请固定为3
        data: 返回的数据实体
        len: 返回的数据实体的长度 
'''
def wrapperCallback(usrTag:str,respData:{},ret:int):
    return


'''
创建会话实例
@param usrTag
    type:str
    desc:用户tag,用于异步关联用户请求
@param params 
	type:	{}
    desc:	功能参数(对应ASE平台上的功能参数)

@param psrIds
	type:	[int]
	desc:	需要使用的个性化资源标识列表(如无个性化需要可忽略)

@param psrCnt 
	type:	int
	desc:	需要使用的个性化资源个数

@param errNum
    type: int
    desc: 错误码


@return handle
	type:	string
	desc:   会话句柄,无错误时返回对应的句柄

'''
def wrapperCreate(usrTag:str,params:{},psrIds:[],psrCnt:int,errNum:int)->str:
    pass


'''
写入相关数据
@param handle
    type:str
    desc: 由wrapperCreate返回的会话句柄

@param  reqData
	type:	[{}] 
	desc:	写入数据实体(对应ASE平台上的请求数据)
        key: 请求数据段的名称
        type: 请求的数据类型 0: 文本 1:音频 2:图像 3:视频 4:个性化数据
        stauts: 数据状态 非流式请固定为3
        data: 请求的数据实体
        len: 请求的数据实体的长度

@return 接口错误码
	type:	int
	desc:	错误码,无错误时返回0
'''
def wrapperWrite(handle:str ,reqData:[])->int:
    pass

'''
写入相关数据
@param handle
    type:str
    desc: 由wrapperCreate返回的会话句柄

@param  respData
	type:	[{}]
	desc:	返回结果实体(对应ASE平台上的响应数据)
        key: 返回数据段的名称
        type: 返回的数据类型 0: 文本 1:音频 2:图像 3:视频 4:个性化数据
        stauts: 数据状态 非流式请固定为3
        data: 返回的数据实体
        len: 返回的数据实体的长度

@return 接口错误码
	type:	int
	desc:	错误码,无错误时返回0
'''
def wrapperRead(handle:str ,respData:[])->int:
    pass


'''
清理此次会话的资源
@param handle
    type:str
    desc: 由wrapperCreate返回的会话句柄
@return 接口错误码
	type:	int
	desc:	错误码,无错误时返回0
'''
def wrapperDestory(handle:str)->int:
    pass
