import React, { useState, useEffect } from 'react';
import { Award, Gift, TrendingUp, Zap, CheckCircle2, RefreshCw } from 'lucide-react';
import api from '../../services/api';

interface LoyaltyAccount {
  points_balance: number;
  lifetime_points_earned: number;
  tier: string;
  cashback_multiplier: number;
}

export const LoyaltyRewardsPortal: React.FC = () => {
  const [account, setAccount] = useState<LoyaltyAccount | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [pointsToRedeem, setPointsToRedeem] = useState<number>(100);

  const fetchLoyalty = async () => {
    setLoading(true);
    try {
      const res = await api.get('/customer-portal/loyalty');
      setAccount(res.data);
    } catch (err) {
      console.error('Failed to load loyalty account', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLoyalty();
  }, []);

  const handleRedeem = async () => {
    try {
      await api.post('/customer-portal/loyalty/redeem', { points_to_redeem: pointsToRedeem });
      fetchLoyalty();
    } catch (err) {
      console.error('Redemption failed', err);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 md:p-10 space-y-8">
      {/* Banner */}
      <div className="border-b border-slate-800 pb-6">
        <h1 className="text-3xl font-extrabold bg-gradient-to-r from-amber-400 via-orange-400 to-yellow-300 bg-clip-text text-transparent">
          Loyalty Rewards & Tier Status
        </h1>
        <p className="text-slate-400 mt-1 text-sm">
          Earn points on every completed repair job, unlock tier perks, and redeem cashback vouchers.
        </p>
      </div>

      {loading ? (
        <div className="flex justify-center py-20">
          <RefreshCw className="w-8 h-8 animate-spin text-amber-500" />
        </div>
      ) : account ? (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Tier Card */}
          <div className="lg:col-span-2 bg-gradient-to-br from-slate-900 via-slate-900 to-amber-950/40 border border-amber-500/20 rounded-3xl p-8 shadow-2xl relative overflow-hidden">
            <div className="absolute -right-10 -bottom-10 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

            <div className="flex items-center justify-between mb-8">
              <div className="flex items-center gap-3">
                <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-2xl">
                  <Award className="w-8 h-8 text-amber-400" />
                </div>
                <div>
                  <span className="text-xs font-semibold text-amber-400 uppercase tracking-widest">Active Status</span>
                  <h2 className="text-2xl font-black text-slate-100">{account.tier} TIER MEMBER</h2>
                </div>
              </div>
              <span className="px-4 py-1.5 text-xs font-bold rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                {account.cashback_multiplier}x Cashback Multiplier
              </span>
            </div>

            <div className="grid grid-cols-2 gap-6 my-8 bg-slate-950/50 border border-slate-800 rounded-2xl p-6">
              <div>
                <span className="text-slate-400 text-xs uppercase font-medium">Available Points Balance</span>
                <p className="text-4xl font-extrabold text-amber-400 mt-1">{account.points_balance}</p>
                <span className="text-xs text-slate-500">Worth ${(account.points_balance * 0.1).toFixed(2)} in discounts</span>
              </div>
              <div>
                <span className="text-slate-400 text-xs uppercase font-medium">Lifetime Points Earned</span>
                <p className="text-4xl font-extrabold text-slate-200 mt-1">{account.lifetime_points_earned}</p>
                <span className="text-xs text-slate-500">Total earned since signup</span>
              </div>
            </div>

            {/* Redeem Box */}
            <div className="flex flex-col sm:flex-row items-center gap-4 bg-slate-900 border border-slate-800 p-4 rounded-xl">
              <input
                type="number"
                value={pointsToRedeem}
                onChange={(e) => setPointsToRedeem(Number(e.target.value))}
                min={10}
                max={account.points_balance}
                className="bg-slate-800 border border-slate-700 rounded-xl px-4 py-2 text-slate-100 w-full sm:w-48 focus:outline-none"
              />
              <button
                onClick={handleRedeem}
                disabled={account.points_balance < pointsToRedeem}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-slate-950 font-bold px-6 py-2.5 rounded-xl transition-all shadow-lg shadow-amber-500/25 disabled:opacity-50"
              >
                <Gift className="w-4 h-4" />
                Redeem Instant Coupon
              </button>
            </div>
          </div>

          {/* Tier Perks */}
          <div className="bg-slate-900/80 border border-slate-800 rounded-3xl p-6 space-y-6">
            <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
              <Zap className="w-5 h-5 text-amber-400" /> Tier Benefits Overview
            </h3>

            <div className="space-y-4 text-sm">
              <div className="p-4 bg-slate-950/60 border border-slate-800/80 rounded-2xl flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <h4 className="font-semibold text-slate-200">Bronze Member (0 - 500 Pts)</h4>
                  <p className="text-slate-400 text-xs mt-1">1.0x points multiplier on all bookings, standard scheduling.</p>
                </div>
              </div>
              <div className="p-4 bg-slate-950/60 border border-slate-800/80 rounded-2xl flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-blue-400 shrink-0 mt-0.5" />
                <div>
                  <h4 className="font-semibold text-slate-200">Silver Member (500 - 1500 Pts)</h4>
                  <p className="text-slate-400 text-xs mt-1">1.25x points multiplier, 5% off spare parts, priority slot booking.</p>
                </div>
              </div>
              <div className="p-4 bg-slate-950/60 border border-slate-800/80 rounded-2xl flex items-start gap-3">
                <CheckCircle2 className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                <div>
                  <h4 className="font-semibold text-slate-200">Gold & Platinum (&gt; 1500 Pts)</h4>
                  <p className="text-slate-400 text-xs mt-1">1.5x points multiplier, 15% spare parts discount, zero diagnostic call-out fee.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
export default LoyaltyRewardsPortal;
