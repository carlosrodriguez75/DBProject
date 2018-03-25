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
        return result


    def getAllUsers(self):
        dao = UsersDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Part=mapped_result)

    def getUsersByUId(self, UID):
        dao = UsersDAO()
        result = dao.getUsersByUId(UID)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Part=mapped)