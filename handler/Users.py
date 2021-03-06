from flask import jsonify, request
from dao.Users import UsersDAO

class UsersHandler:

    def mapToDict(self,row):
        result = {}
        result['UID'] = row[0]
        result['UFirst_Name'] = row[1]
        result['ULast__Name'] = row[2]
        result['UPhone'] = row[3]
        result['UEmail'] = row[4]
        result['UDispName'] = row[5]
        result['UPassword'] = row[6]
        return result

    def mapToDictContactByID(self,row):
        result = {}
        result['UID'] = row[0]
        result['UDispName'] = row[1]
        result['CID'] = row[2]
        result['UContactDispName'] = row[3]
        return result

    def mapToDictUsersByGroup(self,row):
        result = {}
        result['UID'] = row[0]
        result['UDispName'] = row[1]
        return result


    def getAllUsers(self):
        dao = UsersDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getUsersByUId(self, UID):
        dao = UsersDAO()
        result = dao.getUsersByUId(UID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Users=mapped)

    def getUsersByPhone(self,phone):
        dao = UsersDAO()
        result = dao.getUsersByPhone(phone)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getUsersByEmail(self,email):
        dao = UsersDAO()
        result = dao.getUsersByEmail(email)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)

    def getContactsByUserID(self,UID):
        dao = UsersDAO()
        result = dao.getContactsByUserID(UID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictContactByID(r))
            return jsonify(Users=mapped_result)

    def getUsersInGroupChatByID(self,gid):
        dao = UsersDAO()
        result = dao.getUsersInGroupChatByID(gid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictUsersByGroup(r))
            return jsonify(Users=mapped_result)

    def getUsersInGroupChatByName(self,name):
        dao = UsersDAO()
        result = dao.getUsersInGroupChatByName(name)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDictUsersByGroup(r))
            return jsonify(Users=mapped_result)

    def getUserByUsername(self,uname):
        dao = UsersDAO()
        result = dao.getUserByUsername(uname)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Users=mapped_result)
