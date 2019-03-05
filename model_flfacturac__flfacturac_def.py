
# @class_declaration presupuestos_cliente #
from YBUTILS.viewREST import cacheController


class presupuestos_cliente(flfacturac):

    def presupuestos_cliente_bufferCommited_lineaspresupuestoscli(self, curLinea=None):
        # _i = self.iface
        curPresupuesto = qsatype.FLSqlCursor(u"presupuestoscli")
        curPresupuesto.select(ustr(u"idpresupuesto = ", curLinea.valueBuffer(u"idpresupuesto")))
        if not curPresupuesto.first():
            return False
        curPresupuesto.setModeAccess(curPresupuesto.Edit)
        curPresupuesto.refreshBuffer()
        if not qsatype.FactoriaModulos.get('formRecordpresupuestoscli').iface.calcularTotalesCursor(curPresupuesto):
            return False
        if not curPresupuesto.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def bufferCommited_lineaspresupuestoscli(self, curLinea=None):
        return self.ctx.presupuestos_cliente_bufferCommited_lineaspresupuestoscli(curLinea)

